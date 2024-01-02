from django.contrib import admin
from .models import *

# from .models import Hoodie
# from .models import Cargo
# from .models import Jean
# from .models import Oversize
# from .models import Jacket
# Register your models here.


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'active']
#     list_display_links = ['price']
#     list_editable = ['active']
#     search_fields = ['name']
#     list_filter = ['price', 'active']


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Contact)
# admin.site.register(Hoodie, ProductAdmin)
# admin.site.register(Cargo, ProductAdmin)
# admin.site.register(Jean, ProductAdmin)
# admin.site.register(Oversize, ProductAdmin)
# admin.site.register(Jacket, ProductAdmin)


admin.site.site_header = 'Brands Geeks'
admin.site.site_title = 'Brands Geeks'
