"""
URL configuration for rachycentron project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # <-- IMPORTANTE: Adicione esta linha

# Suas URLs principais
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pescadores.urls')),
]

# Este bloco só será executado se DEBUG for True (ou seja, no seu computador)
if settings.DEBUG:
    # A importação é feita aqui dentro para não dar erro em produção
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]