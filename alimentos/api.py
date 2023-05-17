from ninja import Router
from .schemas import Alimento
from .models import Alimento as ModelAlimento
from django.shortcuts import get_object_or_404

alimentos_router = Router()


# @alimentos_router.get('/{alimento_id}/', response = Alimento)
# def get_alimento(request, alimento_id: int) -> Alimento:  
#     alimento = ModelAlimento.objects.get( id = alimento_id)
#     return alimento

@alimentos_router.post('/')
def get_alimento(request, alimento: Alimento):
    return alimento