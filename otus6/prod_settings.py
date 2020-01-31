from .settings import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
# например
ALLOWED_HOSTS = ['otus-university.com']
# etc...
