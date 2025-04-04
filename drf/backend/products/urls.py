from django.urls import path

from products import views # Importando a view ProductDetailView

urlpatterns = [
    path('<int:pk>/',views.ProductDetailAPIView.as_view(), name='product_detail'),  # Detalhes do produto
    path('', views.ProductListCreateAPIView.as_view())
]
