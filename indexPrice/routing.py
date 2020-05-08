from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('index-price', consumers.IndexPriceConsumer),
]
