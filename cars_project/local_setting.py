# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qiwu1og_^@^vrp%a_*1%-s&zq*)1c72pvd5*@hrje4hkr3x0gr'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}