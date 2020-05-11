import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from securitiesManager.models import Security, Price, Weight, Index_price
from .utils import price_of_index

from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import numpy as np


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

        for index in security.index_set.all():
            securities = self.securities_in_index(index)
            securities_prices_weight = np.empty(1, dtype=object)
            for ind, each_security in enumerate(securities):
                prices = self.get_security_prices(each_security)
                weight = self.get_security_index_weight(index, each_security)
                prices_with_weight = prices
                prices_with_weight["weight"] = weight
                if (ind > 0):
                    securities_prices_weight = np.insert(
                        securities_prices_weight, 1, prices_with_weight)
                else:
                    securities_prices_weight[0] = prices_with_weight

            last_index_price = self.get_last_index_price(index)
            current_index_price = price_of_index(
                last_index_price, securities_prices_weight)

            new_index_price = self.insert_index_price(
                index, message["date"], current_index_price)

            self.send(text_data=json.dumps({
                'message': {
                    'indexId': new_index_price.index.id,
                    'indexName': new_index_price.index.name,
                    'date': str(new_index_price.date),
                    'price': new_index_price.price
                }
            }))

        # self.send(text_data=json.dumps({
        # 'message': message
        # }))

    def datetime_to_date(self, current_datetime):
        to_datetime = datetime.strptime(
            current_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')
        return datetime.strftime(to_datetime, "%Y-%m-%d")

    def search_security(self, security_name):
        security, was_created = Security.objects.get_or_create(
            name=security_name
        )
        return security

    def insert_price(self, message, security_obj):
        price, was_created = Price.objects.update_or_create(
            security=security_obj,
            date=self.datetime_to_date(message["date"]),
            defaults={'price': message["price"]},
        )
        return price

    def securities_in_index(self, index):
        return index.securities.all()

    def get_security_prices(self, security_obj):
        last_two_prices = Price.objects.filter(
            security=security_obj).order_by('-date')[:2]
        return {"current": last_two_prices[0].price, "before": last_two_prices[1].price}

    def get_security_index_weight(self, index_obj, security_obj):
        return Weight.objects.get(index=index_obj, security=security_obj).weight

    def get_last_index_price(self, index_obj):
        return Index_price.objects.filter(index=index_obj).order_by('-date')[0].price

    def insert_index_price(self, index_obj, date, price):
        index_price, was_created = Index_price.objects.update_or_create(
            index=index_obj,
            date=self.datetime_to_date(date),
            defaults={'price': price},
        )
        return index_price
