from django.contrib import admin

from .models import Bol
from .models import BolItem
# Register your models here.

admin.site.register(Bol)
admin.site.register(BolItem)