from django import forms  

from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model: Product
        filds = [
            'title',
            'content',
            'price',
            'sale_price',
        ] # Define os campos que serão exibidos no formulário