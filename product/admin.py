from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'lesson', 'get_user_names')

    def get_user_names(self, obj):
        return ", ".join([access.name for access in obj.access_product.all()])

    get_user_names.short_description = "access_product"
