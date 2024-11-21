from django.urls import path
from core.views import failure, make_request

urlpatterns = [
    path('', make_request, name='make-request'),
    path('failure/', failure, name='failure-api')
]