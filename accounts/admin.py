from django.contrib import admin

# Register your models here.
from .models import DeliveryAddress
from .models import DeliveryAddress , Profile , Phones




admin.site.register(Profile)
admin.site.register(Phones)
admin.site.register(DeliveryAddress)