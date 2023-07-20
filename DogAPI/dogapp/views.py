from rest_framework import generics
from dogapp.models import Dog
from dogapp.serializers import DogSerializer

# Create your views here.


class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
