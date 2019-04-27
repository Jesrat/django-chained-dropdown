from .models import *
from rest_framework import serializers


class SubCategoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

