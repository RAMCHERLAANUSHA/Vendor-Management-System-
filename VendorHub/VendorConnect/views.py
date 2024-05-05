from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView

# Create your views here.

class VendorView(APIView):
    def get(self, request, vendor_id = None):
        if id:
            ven = Vendor.objects.get(vendor_code = vendor_id)
            ven1 = VendorSerializer(ven)
            return Response(ven1.data)
        else:
            ven = Vendor.objects.all()
            ven1 = VendorSerializer(ven, many = True)
            return Response(ven1.data)
        
    def post(self, request):
        ven = VendorSerializer(data = request.data)
        if ven.is_valid():
            ven.save()
        return Response({"message":"data saved"})
    
    def put(self, request, vendor_id):
        ven = Vendor.objects.get(vendor_code = vendor_id)
        ven1 = VendorSerializer(ven, data=request.data)
        if ven1.is_valid():
            ven1.save()
        return Response({"message":"data updated"})
    
    def delete(self, request, vendor_id):
        ven =Vendor.objects.get(vendor_code = vendor_id)
        ven.delete()
        return Response({"message":"data deleted"})
    
class PurchaseOrderView(APIView):
    def get(self, request, po_id = None):
        if id:
            order = PurchaseOrder.objects.get(po_number = po_id)
            order1 = PurchaseOrderSerializer(order)
            return Response(order1.data)
        else:
            order = PurchaseOrder.objects.all()
            order1 = PurchaseOrderSerializer(order, many = True)
            return Response(order1.data)
        
    def post(self, request):
        order = PurchaseOrderSerializer(data = request.data)
        if order.is_valid():
            order.save()
        return Response({"message":"data saved"})
    
    def put(self, request, po_id):
        order = PurchaseOrder.objects.get(po_number = po_id)
        order1 = PurchaseOrderSerializer(order, data=request.data)
        if order1.is_valid():
            order1.save()
        return Response({"message":"data updated"})
    
    def delete(self, request, po_id):
        order =PurchaseOrder.objects.get(po_number = po_id)
        order.delete()
        return Response({"message":"data deleted"})
    

class VendorPerformanceView(APIView):
    def get(self, request, po_id = None):
        perform = PurchaseOrder.objects.get(vendor_code = po_id)
        perform1 = PurchaseOrderSerializer(perform)
        return Response(perform1.data)
