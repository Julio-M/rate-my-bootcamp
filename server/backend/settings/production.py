from .base import *

DEBUG = False

# From env
MONGO_DETAILS = config("MONGO_DETAILS")
MONGO_USER = config("MONGO_USER")
MONGO_PASSWORD = config("MONGO_PASSWORD")

DATABASES = {
    'default': {
            'ENGINE': 'djongo',
            'NAME': 'ratemyboot',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': MONGO_DETAILS
            }  

    }
}

#Security settings
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = False #change this when ready to deploy, to access the site over https you need to run the site through a server
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True


