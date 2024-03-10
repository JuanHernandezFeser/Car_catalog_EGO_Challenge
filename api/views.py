from rest_framework import viewsets
from .serializers import CarSerializer
from .models import Car

class CarViewSet(viewsets.ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerializer