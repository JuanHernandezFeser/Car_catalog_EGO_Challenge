from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'car_features', views.CarFeatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]