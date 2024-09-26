from rest_framework import serializers
from products.models import Product

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'is_active',
        )
        read_only_fields = ('id',)