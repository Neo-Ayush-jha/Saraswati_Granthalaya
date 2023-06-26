from rest_framework import serializers
from .models import *
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields="__all__"
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields="__all__"