from ninja import Router
from .schemas import Alimento

alimentos_router = Router()


@alimentos_router.post('/')
def get_alimento(request, alimento: Alimento):    
    return {'titulo': alimento.titulo}