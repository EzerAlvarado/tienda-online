
from products.models import Category
from rest_framework import viewsets
from products.serializers.category import CategoryModelSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class = CategoryModelSerializer