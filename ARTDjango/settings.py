from pathlib import Path

# 项目根路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 密钥 项目默认加密使用
SECRET_KEY = 'django-insecure-812&_grn4hcj%ns!0_(m2+r=(jxqb2$!!qbm_azlbm&0*m7lr('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ip白名单
ALLOWED_HOSTS = []


# 注册app
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册app
    'service.apps.ServiceConfig',
    'component.apps.ComponentConfig'

]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由
ROOT_URLCONF = 'ARTDjango.urls'

# 模板文件存放路径【*】
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# wsgi服务器
WSGI_APPLICATION = 'ARTDjango.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# 静态文件相关配置【*】
import os

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    )

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 自定义枚举值
CODE_MESSAGE = {
    '200':"SUCCESS",
    '201':"Request Failure",
    '500':"SERVER ERROR",
    '404':"Not FOUND",
    '400': "bad request"
}

#日志记录
from loguru import logger
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
#设置主日志文件,所有日志都会记录在此文件中
log_file_path = os.path.join(BASE_DIR, "SysLogs/my.log")# 设置错误日志文件,error级别的日志将会单独记录在此文件中
logger.add(log_file_path, rotation="5 MB", encoding="utf-8")
