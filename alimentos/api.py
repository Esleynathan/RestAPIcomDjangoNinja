from ninja import Router
from django.http import JsonResponse

alimentos_router = Router()

@alimentos_router.get('teste/')
def teste(request):
    return JsonResponse({'teste': 1})