from rest_framework import generics
from rest_framework.decorators import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Product.objects.all() # Define a classe ProductCreateAPIView que herda de CreateAPIView para criar novos produtos
    serializer_class = ProductSerializer # Define a classe ProductCreateAPIView que herda de CreateAPIView para criar novos produtos
    
    def perform_create(self, serializer):  # Sobrescreve o método perform_create para adicionar lógica personalizada ao salvar o produto
        #serializer.save(user=self.request.user)
        print(serializer.validated_data) # Exibe os dados validados no console para depuração
        title = serializer.validated_data('title') 
        content = serializer.validated_data('content') or None # Se o conteúdo não for fornecido, use None como valor padrão
        if content is None:
            content = title
        
        serializer.save(content=content) # Salva o conteúdo como o título se não for fornecido
        
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductListAPIView():
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
@api_view(["GET", "POST"])
def product_alt_view(request, *args, **kwargs):
    method = request.method 
    
    if method == 'GET':
        pass
    
    if method == 'POST':
    