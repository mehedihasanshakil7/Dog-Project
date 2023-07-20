from rest_framework import serializers
from dogapp.models import Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'
