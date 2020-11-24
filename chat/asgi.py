# import os
# import django
# from channels.routing import get_default_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE","chat.settings")
# django.setup()
# application = get_default_application()
import os
import channels 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat.settings_production")
channel_layer = channels.asgi.get_channel_layer()