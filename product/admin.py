from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'lesson', 'get_categories')

    def get_categories(self, obj):
        return ", ".join([access.name for access in obj.access_user.all()])

    get_categories.short_description = "access_user"
