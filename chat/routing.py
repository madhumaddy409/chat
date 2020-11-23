from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from django.urls import re_path

from chat.consumers import ChatConsumer


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path(r'ws/chat/<slug:chatname>/', ChatConsumer),
        ])
    ),
})


