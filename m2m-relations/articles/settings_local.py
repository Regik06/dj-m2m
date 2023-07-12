import os
from website.settings import BASE_DIR

SECRET_KEY = 'b0e@^m&tccz11$w59qov$lhn-97!(%wfn-gray-c*x)^a$wx=2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_m2m_relations',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}