from ninja import NinjaAPI
from alimentos.api import alimentos_router   
from pacientes.api import pacientes_router   
from ninja.parser import Parser
import yaml
from django.http import HttpRequest
from ninja.security import HttpBearer

# class YamlParser(Parser):
#     def parse_body(self, request: HttpRequest):
#         return yaml.safe_load(request.body)

# api = NinjaAPI(parser=YamlParser())

class MyAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str):
        if token == "1234abc":
            return token

api = NinjaAPI(auth=MyAuth())

api.add_router('/alimentos', alimentos_router)
api.add_router('/pacientes', pacientes_router)