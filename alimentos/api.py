from ninja import Router, Schema
from typing import List, Dict
# from django.http import JsonResponse

alimentos_router = Router()

class Alimento(Schema):
    titulo: str
    quantidade: int
    variedades: Dict[str, int]

# alimentos = [{'Nome': 'Banana', 'Quantidade': 5, 'id': 1},
#            {'Nome': 'Carne', 'Quantidade': 15, 'id': 2},
#            {'Nome': 'Maçã', 'Quantidade': 2, 'id': 3},# ]

# @alimentos_router.get('/{int:alimento_id}/')
# def get_alimento(request, alimento_id: int, preco_min: int = 10):
#     return {'alimento.id': alimento_id, 'preco_min': preco_min}

@alimentos_router.post('/')
def get_alimento(request, alimento: Alimento):
    # print(alimento.titulo)
    # print(alimento.quantidade)
    
    return {'variedade': alimento.variedades}