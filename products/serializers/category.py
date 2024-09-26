from rest_framework import serializers
from products.models import Category

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )
        read_only_fields = ('id',)