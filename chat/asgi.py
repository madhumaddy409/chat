# import os
# import django
# from channels.routing import get_default_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE","chat.settings")
# django.setup()
# application = get_default_application()
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "routeradmin.settings_production")

from channels.asgi import get_channel_layer

channel_layer = get_channel_layer()