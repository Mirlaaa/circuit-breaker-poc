from django.urls import path
from core.views import failure

urlpatterns = [
    path('failure/', failure, name="failure-api",)
]