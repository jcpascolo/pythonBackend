from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
import securitiesManager.consumers
import indexPrice.consumers

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('index-price', indexPrice.consumers.IndexPriceConsumer),
            path('security-price', securitiesManager.consumers.SecurityPriceConsumer),
        ])
    )
})
