import time
import random
import requests
from http import HTTPStatus
from django.http import JsonResponse
from core.circuit_breaker import breaker, CIRCUIT_BREAKER_ERROR

@breaker
def make_request(request):
    try:
        for i in range(0, 11):
            endpoint = 'failure/' if i % 2 == 0 else 'slower_request/'
            response = requests.get(endpoint, timeout=0.1)
            response.raise_for_status()
            return JsonResponse(response.json())
    except CIRCUIT_BREAKER_ERROR:
        return JsonResponse(data={"message":"Service is down"}, status=HTTPStatus.SERVICE_UNAVAILABLE)


def failure(request):
    return JsonResponse(data={"message":"Failure"}, status=HTTPStatus.OK)

def slower_request(request):
    random_value = random.randint(0,1)

    if random_value == 0:
        time.sleep(2)  

    return JsonResponse(data={"message":"Successful request!"}, status=HTTPStatus.OK)

def success(request):
    return JsonResponse(data={"message":"Successful request!"}, status=HTTPStatus.OK)

