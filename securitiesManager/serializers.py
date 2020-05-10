from rest_framework import serializers

from .models import Index, Index_price, Price, Security, Weight


class IndexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Index
        fields = ('id', 'name', 'securities')


class IndexPriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Index_price
        fields = ('id', 'index', 'date', 'price')


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'security', 'date', 'price')


class SecuritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Security
        fields = ('id', 'name')


class WeightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weight
        fields = ('id', 'index', 'security', 'weight')
