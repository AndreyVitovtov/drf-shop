from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Manager)
admin.site.register(models.Customer)
admin.site.register(models.DeliveryCrew)
admin.site.register(models.Cart)
