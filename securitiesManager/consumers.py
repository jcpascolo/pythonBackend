import json
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from securitiesManager.models import Security, Price

from django.core.exceptions import ObjectDoesNotExist


class SecurityPriceConsumer(WebsocketConsumer):
    def connect(self):
        print("Request received")
        self.accept()

    def disconnect(self, close_code):
        print("Disconnected")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        received_security_name = message['securityName']
        security = self.search_security(received_security_name)

        self.insert_price(message, security)

        # self.send({
        # "type": "websocket.send",
        # "text": "An error have ocurred"
        # })

        # self.send(text_data=json.dumps({
        # 'message': message
        # }))

    def search_security(self, security_name):
        security, was_created = Security.objects.get_or_create(
            name=security_name
        )
        return security

    def insert_price(self, message, security_obj):
        price = Price(security=security_obj,
                      date=message["date"], price=message["price"])
        price.save()
        return price
