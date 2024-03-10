from django.urls import path,include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'cars',views.CarViewSet)

urlpatterns=[
    path('', include(router.urls))
]