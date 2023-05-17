from ninja import Router
from django.http import JsonResponse

alimentos_router = Router()

@alimentos_router.get('/{int:alimento_id}/')
def get_alimento(request, alimento_id: int):
    return JsonResponse({'id': alimento_id})