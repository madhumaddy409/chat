import os

from django.core.asgi import get_asgi_application
from dj_static import Cling


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

# application = get_wsgi_application()
application = get_asgi_application()