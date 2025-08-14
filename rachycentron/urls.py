# Arquivo: rachycentron/urls.py (VERSÃO FINAL E CORRETA)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # <-- Importa as configurações do Django

# Suas URLs principais que devem funcionar em produção
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pescadores.urls')),
]

# Este bloco só será executado se settings.DEBUG for True (no seu computador)
# O Render (onde DEBUG é False) vai ignorar completamente este bloco.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]