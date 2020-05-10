from rest_framework import viewsets

from .serializers import IndexSerializer, IndexPriceSerializer, PriceSerializer,  SecuritySerializer, WeightSerializer
from .models import Index, Index_price, Price, Security, Weight


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer


class IndexPriceViewSet(viewsets.ModelViewSet):
    queryset = Index_price.objects.all()
    serializer_class = IndexPriceSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class SecurityViewSet(viewsets.ModelViewSet):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer


class WeightViewSet(viewsets.ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
