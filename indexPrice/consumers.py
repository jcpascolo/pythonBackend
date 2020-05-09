import json
from channels.generic.websocket import WebsocketConsumer


class IndexPriceConsumer(WebsocketConsumer):
    def connect(self):
        print("Request received in index")
        self.accept()

    def disconnect(self, close_code):
        print("Disconnected from index")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

    def test_channel(self, event):
        print("Index with channel")
