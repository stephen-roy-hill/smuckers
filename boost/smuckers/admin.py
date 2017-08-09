from django.contrib import admin

from.models import Bol, BolItem, ForkliftDriver, TruckDriver, SentEmail, Weight
# Register your models here.

admin.site.register(Bol)
admin.site.register(BolItem)
admin.site.register(ForkliftDriver)
admin.site.register(TruckDriver)
admin.site.register(SentEmail)
admin.site.register(Weight)