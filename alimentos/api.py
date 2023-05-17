from ninja import Router
from django.http import JsonResponse
from typing import List,Dict

alimentos_router = Router()


alimentos = [
    {'Nome': 'Banana', 'Quantidade': 5, 'id': 1},
    {'Nome': 'Carne', 'Quantidade': 15, 'id': 2},
    {'Nome': 'Maçã', 'Quantidade': 2, 'id': 3},
]

@alimentos_router.get('/{int:alimento_id}/')
def get_alimento(request, alimento_id: int, preco_min: int = 10):
    return {'alimento.id': alimento_id, 'preco_min': preco_min}