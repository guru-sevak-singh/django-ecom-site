from django.contrib import admin
from .models import Product, Order

# custamize the django admin panal
admin.site.site_header = 'My E-Comerce Site Panal'
admin.site.site_title = 'E-Comerce Site'
admin.site.index_title = 'guru'

class ProductAdmin(admin.ModelAdmin):
    def change_catogary_to_default(self, request, quesryset):
        quesryset.update(catogary='default')

    change_catogary_to_default.short_description = 'Set Default'
    list_display = ('name', 'price','discount_price', 'catogary', 'description')
    search_fields = ('name', 'catogary')
    actions = ('change_catogary_to_default', )
    list_editable = ('price', 'catogary' )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
