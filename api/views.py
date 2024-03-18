from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CarSerializer, CategorySerializer
from .models import Car, Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class CarViewSet(viewsets.ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'])
    def order_by_price_asc(self, request):
        ordered_cars = Car.objects.all().order_by('price')
        serializer = self.get_serializer(ordered_cars, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def order_by_price_desc(self, request):
        ordered_cars = Car.objects.all().order_by('-price')
        serializer = self.get_serializer(ordered_cars, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def order_by_year_asc(self, request):
        ordered_cars = Car.objects.all().order_by('year')
        serializer = self.get_serializer(ordered_cars, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def order_by_year_desc(self, request):
        ordered_cars = Car.objects.all().order_by('-year')
        serializer = self.get_serializer(ordered_cars, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def order_by_brand_asc(self, request):
        ordered_cars = Car.objects.all().order_by('brand')
        serializer = self.get_serializer(ordered_cars, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def order_by_brand_desc(self, request):
        ordered_cars = Car.objects.all().order_by('-brand')
        serializer = self.get_serializer(ordered_cars, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def filter_by_category(self, request):
        category_id = request.query_params.get('category_id')
        filtered_cars = Car.objects.filter(category_id=category_id)
        serializer = self.get_serializer(filtered_cars, many=True)
        return Response(serializer.data)