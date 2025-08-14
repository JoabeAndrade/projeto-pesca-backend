"""
Django settings for rachycentron project.
"""

import dj_database_url
import os
from pathlib import Path
# 1. Importa a biblioteca para ler o arquivo .env
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Carrega as variáveis de ambiente do arquivo .env (só funciona localmente)
# No Render, ele vai ignorar isso e usar as variáveis de ambiente do próprio Render.
load_dotenv(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# Lê a SECRET_KEY do ambiente (seja do .env local ou do Render)
SECRET_KEY = os.environ.get('SECRET_KEY')

# DEBUG é False em produção (no Render) e True localmente
DEBUG = 'RENDER' not in os.environ

# Configuração de ALLOWED_HOSTS para o Render e desenvolvimento local
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'pescadores',
    'debug_toolbar',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 3. Configuração do WhiteNoise para servir arquivos estáticos em produção
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Adiciona o middleware do debug_toolbar apenas se DEBUG for True
if DEBUG:
    MIDDLEWARE.insert(MIDDLEWARE.index('django.middleware.common.CommonMiddleware'), 'debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'rachycentron.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rachycentron.wsgi.application'

# 4. Database configurado para ler a DATABASE_URL do ambiente
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require='RENDER' in os.environ # Exige SSL apenas no Render
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# --- CONFIGURAÇÕES FINAIS PARA PRODUÇÃO E DESENVOLVIMENTO ---

# 5. CORS: Configuração dinâmica para permitir o frontend da Vercel e o localhost
FRONTEND_URL = os.environ.get('FRONTEND_URL')
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
if FRONTEND_URL:
    CORS_ALLOWED_ORIGINS.append(FRONTEND_URL)

# 6. Static Files: Configuração para o WhiteNoise servir CSS/JS em produção
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'