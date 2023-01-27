from django.contrib import admin
from .models import Product
from django.utils.safestring import mark_safe
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","description","price","image","create_date","viewer","button")

    def button(self, obj):
        return mark_safe(f'<a class="button" href={obj} >Кнопка</a>')


admin.site.register(Product,ProductAdmin)




