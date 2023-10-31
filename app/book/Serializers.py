from rest_framework.serializers import ModelSerializer
from .models import *


class BookSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'photo', 'sale', 'count_product', 'slug', 'author', 'category']


class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Authors
        fields = "__all__"
