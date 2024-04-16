import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from main import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    # (HTTP)
    "http": get_asgi_application(),
    # WebSocket
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    ),
})
