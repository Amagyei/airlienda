"""
Django settings for airlienda project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from environs import Env 
env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_5xe6^d9wcnr&4wzy6^+9a=v3x5qtyty155noj8_l4n!hng3+d"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
SECURE_CROSS_ORIGIN_OPENER_POLICY=' same-origin-allow-popups'


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # custom apps
    "airlienda",
    "hostel",
    "rooms",
    "userauth", 
    "addon",
    "booking.apps.BookingConfig",
    "userDashboard",

    # third party apps
    "taggit",
    #  "crispy-forms",
    "shortuuid",
    "import_export",
    "anymail",
    "mathfilters",
    "ckeditor_uploader",
    "django_ckeditor_5",
    'debug_toolbar',
    'stripe',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "airlienda.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "airlienda.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)s
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'global_static')]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# 
# USER AUTH SETTINGS
# 

AUTH_USER_MODEL = "userauth.User"

LOGIN_URL = 'userauth:sign-in'
LOGOUT_REDIRECT = 'userauth:sign-in'

# 
# STRIPE SETTINGS
# 

STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_PUBLIC_KEY = env("STRIPE_PUBLIC_KEY")


#
# PAYSTACK SETTINGS
# 

PAYSTACK_PUBLIC_KEY = env('PAYSTACK_PUBLIC_KEY')
PAYSTACK_SECRET_KEY = env('PAYSTACK_SECRET_KEY')


# 
# JAZZMIN SETTINGS
# 
JAZZMIN_SETTINGS = {
    "site_header": "Airlienda",
    "site_brand": "Room Management at your fingertips",
    "site_logo": "/images/logo-png",
    "copyright": "All Rights Reserved 2023",
    "welcome_sign": "Welcome to Airlienda, Login Now.",
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Company", "url": "/admin/addons/company/"},
        {"name": "Users", "url": "/admin/userauths/user/"},
        {"model": "AUTH_USER_MODEL.User"},
    ],
    "order_with_respect_to": {
        "hostel",
        "hostel.Hostel",
        "hostel.Room",
        "hostel.Booking",
        "hostel.BookingDetail",
        "hostel.Guest",
        "hostel.RoomServices",
        "userauths",
        "addons",
    },
    "icons": {
        "admin.LogEntry": "fas fa-file",
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "userauths.User": "fas fa-user",
        "userauths.Profile": "fas fa-address-card",
        "hostel.hostel": "fas fa-th",
        "hostel.Booking": "fas fa-calendar-week",
        "hostel.BookingDetail": "fas fa-calendar-alt",
        "hostel.Guest": "fas fa-user",
        "hostel.Room": "fas fa-bed",
        "hostel.RoomServices": "fas fa-user-cog",
        "hostel.Notification": "fas fa-bell",
        "hostel.Coupon": "fas fa-tag",
        "hostel.Bookmark": "fas fa-heart",
    },
    "JAZZMIN_UTTWEAKS": {
        "navbar_small_text": False,
        "footer_small_text": False,
        "body_small_text": True,
        "brand_small_text": False,
        "brand_colour": "navbar-indigo",
        "accent": "accent-olive",
        "navbar": "navbar-indigo navbar-dark",
        "no_navbar_border": False,
        "navbar_fixed": False,
        "layout_boxed": False,
        "footer_fixed": False,
        "sidebar_fixed": False,
        "sidebar": "sidebar-dark-indigo",
        "sidebar_nav_small_text": False,
        "sidebar_disable_expand": False,
        "sidebar_nav_child_indent": False,
        "sidebar_nav_compact_style": False,
        "sidebar_nav_legacy_style": False,
        "sidebar_nav_flat_style": False,
        "theme": "cyborg",
        "dark_mode_theme": "cyborg",
        "button_classes": {
            "primary": "btn-primary",
            "secondary": "btn-secondary",
            "info": "btn-info",
            "warning": "btn-warning",
            "danger": "btn-danger",
            "success": "btn-success",
        }
    }
}


INTERNAL_IPS = [
    '127.0.0.1',
]

