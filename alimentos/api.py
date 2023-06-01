from ninja import Router
# from .schemas import Alimento
# from .models import Alimento as ModelAlimento
# from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
from time import sleep
from ninja.security import HttpBearer

# @alimentos_router.get('/{alimento_id}/', response = Alimento)
# def get_alimento(request, alimento_id: int) -> Alimento:  
#     alimento = ModelAlimento.objects.get( id = alimento_id)
#     return alimento

# @alimentos_router.post('/')
# def get_alimento(request, alimento: Alimento):
#     print(alimento.quantidade)
#     return {'quantidade': alimento.quantidade}

alimentos_router = Router()

class MyAuth2(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str):
        if token == "xyz":
            return token

@alimentos_router.get('/', auth=MyAuth2)
def get_alimento(request, response: HttpResponse):

    return{'quantidade': 1}