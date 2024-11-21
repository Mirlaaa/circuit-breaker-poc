import time
import random
import requests
from http import HTTPStatus
from django.http import JsonResponse
from core.circuit_breaker import breaker, CIRCUIT_BREAKER_ERROR
from django.conf import settings

HOST_SERVER = settings.HOST_SERVER

@breaker
def call_endpoint():    
    endpoint = 'failure'
    
    if breaker.current_state == "half-open":
        if breaker.fail_counter >= 4:
            endpoint = 'success'

    response = requests.get(f'{HOST_SERVER}/{endpoint}/')
    response.raise_for_status()

    return response

def failure(request):
    return JsonResponse(data={"message":"Failure"}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

def slower_request(request):
    random_value = random.randint(0,1)

    if random_value == 0:
        time.sleep(2)  

    return JsonResponse(data={"message":"Successful request!"}, status=HTTPStatus.OK)

def success(request):
    return JsonResponse(data={"message":"Successful request!"}, status=HTTPStatus.OK)

def index(request):
    try:
        response = call_endpoint()
        return JsonResponse(data=response.json(), status=response.status_code)
    except CIRCUIT_BREAKER_ERROR:
        return JsonResponse(data={"message":"Circuit breaker is open!"}, status=HTTPStatus.SERVICE_UNAVAILABLE)
    except Exception as e:
        print(f'Error: {e}')
        return JsonResponse(data={"message":"Internal server error!"}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
