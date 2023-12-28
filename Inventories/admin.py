from django.contrib import admin
from .models import Colors, Size, Category, Items

# Register your models here.

admin.site.register(Colors)

admin.site.register(Size)

admin.site.register(Category)

class ItemsAdmin(admin.ModelAdmin):
    list_display = ("admin_name", "quantity", "color", "size", "category", "update_Date")
admin.site.register(Items, ItemsAdmin)