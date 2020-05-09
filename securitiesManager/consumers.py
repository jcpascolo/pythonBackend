import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from securitiesManager.models import Security, Price

from django.core.exceptions import ObjectDoesNotExist


class SecurityPriceConsumer(WebsocketConsumer):
    def connect(self):
        print("Request received")
        self.channel_layer.group_add("security_manage", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        print("Disconnected")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        received_security_name = message['securityName']
        security = self.search_security(received_security_name)

        self.insert_price(message, security)

        print("SELF:")
        print(self.channel_name)

        async_to_sync(self.channel_layer.group_send)("security_manage", {
            "type": "test.channel",
            "message": "In the channel"
        })

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

    def test_channel(self, event):
        print("SELF CHANNEL")
