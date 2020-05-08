from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('security-price', consumers.SecurityPriceConsumer),
]
