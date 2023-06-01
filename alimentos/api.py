from ninja import Router
# from .schemas import Alimento
# from .models import Alimento as ModelAlimento
# from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
from time import sleep

# @alimentos_router.get('/{alimento_id}/', response = Alimento)
# def get_alimento(request, alimento_id: int) -> Alimento:  
#     alimento = ModelAlimento.objects.get( id = alimento_id)
#     return alimento

# @alimentos_router.post('/')
# def get_alimento(request, alimento: Alimento):
#     print(alimento.quantidade)
#     return {'quantidade': alimento.quantidade}

alimentos_router = Router()

@alimentos_router.get('/')
def get_alimento(request, response: HttpResponse):

    return{'quantidade': 1, 'request': request.auth}