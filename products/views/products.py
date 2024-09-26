
from products.models import Product
from rest_framework import viewsets
from products.serializers.products import ProductModelSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductModelSerializer