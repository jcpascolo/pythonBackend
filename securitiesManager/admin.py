from django.contrib import admin
from .models import Index, Index_price, Price, Security, Weight

admin.site.register(Index)
admin.site.register(Index_price)
admin.site.register(Price)
admin.site.register(Security)
admin.site.register(Weight)
