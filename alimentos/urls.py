from django.urls import path, include
from .api.api import api


urlpatterns = [
    path('', api.urls)
]
