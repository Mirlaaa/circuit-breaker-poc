from django.urls import path
from core.views import index, failure, slower_request, success

urlpatterns = [
    path('', index, name='make-request-api'),
    path('failure/', failure, name='failure-api'),
    path('slower/', slower_request, name='slower-api'),
    path('success/', success, name='success-api'),
]