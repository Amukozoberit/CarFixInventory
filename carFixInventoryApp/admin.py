from django.contrib import admin

from carFixInventoryApp.models import Mechanic,Service,ShopInventory

# Register your models here.


admin.site.register(ShopInventory)
# admin.site.register(Mechanic)
# admin.site.register(ServicesTable)
admin.site.register(Mechanic)
admin.site.register(Service)