from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views

# Configuración del router para tu API
router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('categories', views.CategoryViewSet, basename='categories')

urlpatterns = [
    path('admin/', admin.site.urls),  # Asegúrate de incluir el admin aquí
    path('', include(router.urls)),  # Incluye las rutas del API
]
