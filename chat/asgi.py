# import os
# import django
# from channels.routing import get_default_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE","chat.settings")
# django.setup()
# application = get_default_application()

import os

from channels.routing import ProtocolTypeRouter
# from django.core.asgi import get_asgi_application

from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

application = ProtocolTypeRouter({
    "http": channel_layer,
    # Just HTTP for now. (We can add other protocols later.)
})