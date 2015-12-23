from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nih62dv737s0f6k!f$c1_gz(a5u2lp*zn&zvphwc&m@e-l*z8s'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'