from django.contrib import admin
from user.models import User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname',)
