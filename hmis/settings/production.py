from hmis.settings.base import *
import json
with open('/etc/config.json') as config_file:
        config = json.load(config_file)

DEBUG = True
ALLOWED_HOSTS = ['communitygis.net', 'hmis.communitygis.net', '65.0.224.219','3.109.54.143']
SECRET_KEY = config['SECRET_KEY'] 

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config['DBNAME'],
        'USER': config['DBUSER'],
        'PASSWORD': config['DBPASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}