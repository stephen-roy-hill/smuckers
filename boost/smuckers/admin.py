from django.contrib import admin

from .models import Bol
from .models import BolItem
from.models import ForkliftDriver
# Register your models here.

admin.site.register(Bol)
admin.site.register(BolItem)
admin.site.register(ForkliftDriver)