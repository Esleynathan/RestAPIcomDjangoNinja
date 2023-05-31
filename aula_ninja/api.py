from ninja import NinjaAPI
from alimentos.api import alimentos_router   
from pacientes.api import pacientes_router   
from ninja.parser import Parser
import yaml
from django.http import HttpRequest

class YamlParser(Parser):
    def parse_body(self, request: HttpRequest):
        return yaml.safe_load(request.body)


api = NinjaAPI(parser=YamlParser())

api.add_router('/alimentos', alimentos_router)
api.add_router('/pacientes', pacientes_router)