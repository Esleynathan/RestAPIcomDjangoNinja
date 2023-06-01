from ninja import NinjaAPI
from alimentos.api import alimentos_router   
from pacientes.api import pacientes_router 
from django.http import HttpRequest

from ninja.security import HttpBasicAuth

class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        if username == "admin" and password =="1234":
            return 1

api = NinjaAPI(auth=BasicAuth())

api.add_router('/alimentos', alimentos_router)
api.add_router('/pacientes', pacientes_router)