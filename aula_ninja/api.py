from ninja import NinjaAPI
from alimentos.api import alimentos_router   
from pacientes.api import pacientes_router 
from django.http import HttpRequest
from django.contrib import auth

from ninja.security import HttpBasicAuth

class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        user = auth.authenticate(username=username, password=password)

        if user:
            return user.id

api = NinjaAPI(auth=BasicAuth())
 
api.add_router('/alimentos', alimentos_router)
api.add_router('/pacientes', pacientes_router)