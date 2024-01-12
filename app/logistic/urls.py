from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProductViewSet, StockViewSet, health_check

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path('', health_check, name='health_check'),
    ]

urlpatterns.extend(router.urls)
