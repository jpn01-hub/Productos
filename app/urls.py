from django.urls import path
from .views import crear_producto, listar_productos

urlpatterns = [
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
]