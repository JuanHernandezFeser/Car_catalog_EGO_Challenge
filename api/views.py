from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CarSerializer, CategorySerializer, CarFeatureSerializer
from .models import Car, Category, CarFeature

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class CarViewSet(viewsets.ModelViewSet):
    # queryset=Car.objects.all()
    queryset = Car.objects.prefetch_related('carfeature_set').all()
    serializer_class=CarSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'])
    def filter_and_order(self, request):
        category_id = request.query_params.get('category_id')
        order_by = request.query_params.get('order_by', 'price')
        order_direction = request.query_params.get('order_direction', 'asc')
        
        # Filtrar por categoría si se proporciona category_id
        if category_id:
            queryset = self.queryset.filter(category_id=category_id)
        else:
            queryset = self.queryset
        
        # Aplicar ordenamiento
        if order_by == 'price':
            queryset = queryset.order_by(f'{"" if order_direction == "asc" else "-"}price')
        elif order_by == 'year':
            queryset = queryset.order_by(f'{"" if order_direction == "asc" else "-"}year')
        else:
            return Response({'error': 'Invalid order_by parameter'}, status=400)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class CarFeatureViewSet(viewsets.ModelViewSet):
    queryset=CarFeature.objects.all()
    serializer_class=CarFeatureSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)