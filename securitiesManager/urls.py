from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'indexes', views.IndexViewSet)
router.register(r'indexes_prices', views.IndexPriceViewSet)
router.register(r'prices', views.PriceViewSet)
router.register(r'securities', views.SecurityViewSet)
router.register(r'weights', views.WeightViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
