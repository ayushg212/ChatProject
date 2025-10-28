import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatProject.settings')
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatapp.routing  






application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatapp.routing.websocket_urlpatterns
        )
    ),
})
