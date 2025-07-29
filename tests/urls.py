from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OposicionViewSet,
    TemaViewSet,
    PreguntaViewSet,
    ResultadoTestViewSet
)

# El router crea automáticamente las URLs para Oposiciones, Temas, etc.
router = DefaultRouter()
router.register(r'oposiciones', OposicionViewSet, basename='oposicion')
router.register(r'temas', TemaViewSet, basename='tema')
router.register(r'preguntas', PreguntaViewSet, basename='pregunta')
router.register(r'resultados', ResultadoTestViewSet, basename='resultado')

# Este archivo ahora SOLO exporta las rutas del router.
urlpatterns = [
    path('', include(router.urls)),
]
