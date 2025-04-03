from django.http import JsonResponse
from products.models import Product

from django.forms.models import model_to_dict 

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer #importando o serializer do produto

@api_view(["GET"]) #decorador que define que a funcao aceita apenas o metodo GET
def api_home(request, *args, **kwargs): #definindo a funcao api_home, que recebe um request e argumentos adicionais
    instance = Product.objects.all().order_by("?").first()
    data = {} #preenchendo com dicionario vazio
    if instance: #verifica se existe algum dado no banco de dados
        #data = Product#converte o objeto em dicionario, pegando apenas os campos id, title e price
        data = ProductSerializer(instance).data
        
    return Response(data) #retorna um JsonResponse com a mensagem "Hi, there!" e os dados do produto