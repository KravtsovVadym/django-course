# >---------------------------------------<
# (Django Project Settings) --------------<
# >---------------------------------------<

from pathlib import Path
from decouple import config
import cloudinary
import cloudinary.uploader
import cloudinary.api

# >---------------------------------------<
# (Base Configuration) -------------------<
# >---------------------------------------<

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = []

# >---------------------------------------<
# (Application Definition) ---------------<
# >---------------------------------------<

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "accounts",  # Custom user authentication
    "weblog",    # Blog functionality
]

# Custom user model
AUTH_USER_MODEL = "accounts.User"

# >---------------------------------------<
# (Middleware Configuration) -------------<
# >---------------------------------------<

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

# >---------------------------------------<
# (Templates Configuration) --------------<
# >---------------------------------------<

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"

# >---------------------------------------<
# (Database Configuration) ---------------<
# >---------------------------------------<

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "development",
        "USER": "ubuntu",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# >---------------------------------------<
# (Password Validation) ------------------<
# >---------------------------------------<

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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

# >---------------------------------------<
# (Internationalization) -----------------<
# >---------------------------------------<

# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Kyiv"

USE_I18N = True

USE_TZ = True

# >---------------------------------------<
# (Static Files Configuration) -----------<
# >---------------------------------------<

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "/static/"  # URL prefix for static files
STATIC_ROOT = BASE_DIR / "staticfiles"  # Production static files location
STATICFILES_DIRS = [  # Development static files directories
    BASE_DIR / "static"
]

# >---------------------------------------<
# (Authentication Settings) --------------<
# >---------------------------------------<

# Redirection when you log out of your account
LOGOUT_REDIRECT_URL = "accounts:login"

# >---------------------------------------<
# (Cloudinary Configuration) -------------<
# >---------------------------------------<

cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME"),
    api_key=config("CLOUDINARY_API_KEY"),
    api_secret=config("CLOUDINARY_API_SECRET"),
)