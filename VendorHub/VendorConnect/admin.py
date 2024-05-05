from django.contrib import admin
from .models import Vendor
from .models import PurchaseOrder
# Register your models here.

"""
Registers models with the Django admin interface.

- Vendor: This registers the Vendor model with the Django admin interface, allowing administrators to view, add, edit, and delete vendor data through the admin panel.
- PurchaseOrder: This registers the PurchaseOrder model with the Django admin interface, allowing administrators to view, add, edit, and delete purchase order data through the admin panel.
"""

admin.site.register(Vendor)
admin.site.register(PurchaseOrder)

