import time
import random
import requests
from django.http import JsonResponse
from circuit_breaker import breaker

@breaker
def make_request(request):
    for i in range(0, 11):
        endpoint = 'failure/' if i % 2 == 0 else 'slower_request/'
        response = requests.get(endpoint, timeout=0.1)
        response.raise_for_status()
        return JsonResponse(response.json())

def failure(request):
    return JsonResponse(data={"error":"Failure"}, status=500)

def slower_request(request):
    random_value = random.randint(0,1)

    if random_value == 0:
        time.sleep(2)  

    return JsonResponse(data={"message":"Successful request!"}, status=200)

def success(request):
    return JsonResponse(data={"message":"Successful request!"}, status=200)

