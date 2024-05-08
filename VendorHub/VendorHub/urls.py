"""
URL configuration for VendorHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from VendorConnect import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


    # Vendor API endpoints
    path('GET/api/vendors/',views.VendorView.as_view()),
    path('GET/api/vendors/<int:vendor_id>',views.VendorView.as_view()),
    path('POST/api/vendors',views.VendorView.as_view()),
    path('PUT/api/vendors/<int:vendor_id>',views.VendorView.as_view()),
    path('DELETE/api/vendors/<int:vendor_id>',views.VendorView.as_view()),

    # Purchase Order API endpoints
    path('GET/api/purchase_orders/',views.PurchaseOrderView.as_view()),
    path('GET/api/purchase_orders/<int:po_id>',views.PurchaseOrderView.as_view()),
    path('POST/api/purchase_orders',views.PurchaseOrderView.as_view()),
    path('PUT/api/purchase_orders/<int:po_id>',views.PurchaseOrderView.as_view()),
    path('DELETE/api/purchase_orders/<int:po_id>',views.PurchaseOrderView.as_view()),

    # Vendor performance API endpoint
    path('GET/api/vendors/<int:vendor_id>/performance',views.VendorPerformanceView.as_view()),

]
