from django.urls import path,include
from rest_framework import routers
from api import views


cars_router=routers.DefaultRouter()
cars_router.register(r'cars',views.CarViewSet)

category_router=routers.DefaultRouter()
category_router.register(r'category',views.CategoryViewSet)

urlpatterns=[
    path('cars/', include(cars_router.urls)),
    path('categories/', include(category_router.urls))
]