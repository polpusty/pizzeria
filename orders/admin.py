from django.contrib import admin

from .models import Pizza, Component, Order, PizzaOrder

admin.site.register(Pizza, admin.ModelAdmin)
admin.site.register(Component, admin.ModelAdmin)
admin.site.register(Order, admin.ModelAdmin)
admin.site.register(PizzaOrder, admin.ModelAdmin)
