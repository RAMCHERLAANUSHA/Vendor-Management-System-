from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView

# Create your views here.

class VendorView(APIView):

    """
    API endpoint for vendor operations.

    - GET: Retrieve vendor(s)
    - POST: Create a new vendor
    - PUT: Update an existing vendor
    - DELETE: Delete a vendor
    """

    def get(self, request, vendor_id = None):

        """
        Retrieve vendor details.

        Parameters:
        - vendor_id: The vendor code (optional)

        Returns:
        - Response with vendor data
        """

        if id:
            ven = Vendor.objects.get(vendor_code = vendor_id)
            ven1 = VendorSerializer(ven)
            return Response(ven1.data)
        else:
            ven = Vendor.objects.all()
            ven1 = VendorSerializer(ven, many = True)
            return Response(ven1.data)
        
    def post(self, request):

        """
        Create a new vendor.

        Parameters:
        - request.data: Vendor data

        Returns:
        - Response with success message
        """

        ven = VendorSerializer(data = request.data)
        if ven.is_valid():
            ven.save()
        return Response({"message":"data saved"})
    
    def put(self, request, vendor_id):

        """
        Update an existing vendor.

        Parameters:
        - vendor_id: The vendor code
        - request.data: Updated vendor data

        Returns:
        - Response with success message
        """

        ven = Vendor.objects.get(vendor_code = vendor_id)
        ven1 = VendorSerializer(ven, data=request.data)
        if ven1.is_valid():
            ven1.save()
        return Response({"message":"data updated"})
    
    def delete(self, request, vendor_id):

        """
        Delete a vendor.

        Parameters:
        - vendor_id: The vendor code

        Returns:
        - Response with success message
        """

        ven =Vendor.objects.get(vendor_code = vendor_id)
        ven.delete()
        return Response({"message":"data deleted"})
    
class PurchaseOrderView(APIView):

    """
    API endpoint for purchase order operations.

    - GET: Retrieve purchase order(s)
    - POST: Create a new purchase order
    - PUT: Update an existing purchase order
    - DELETE: Delete a purchase order
    """

    def get(self, request, po_id = None):

        """
        Retrieve purchase order details.

        Parameters:
        - po_id: The purchase order number (optional)

        Returns:
        - Response with purchase order data
        """

        if id:
            order = PurchaseOrder.objects.get(po_number = po_id)
            order1 = PurchaseOrderSerializer(order)
            return Response(order1.data)
        else:
            order = PurchaseOrder.objects.all()
            order1 = PurchaseOrderSerializer(order, many = True)
            return Response(order1.data)
        
    def post(self, request):

        """
        Create a new purchase order.

        Parameters:
        - request.data: Purchase order data

        Returns:
        - Response with success message
        """

        order = PurchaseOrderSerializer(data = request.data)
        if order.is_valid():
            order.save()
        return Response({"message":"data saved"})
    
    def put(self, request, po_id):

        """
        Update an existing purchase order.

        Parameters:
        - po_id: The purchase order number
        - request.data: Updated purchase order data

        Returns:
        - Response with success message
        """

        order = PurchaseOrder.objects.get(po_number = po_id)
        order1 = PurchaseOrderSerializer(order, data=request.data)
        if order1.is_valid():
            order1.save()
        return Response({"message":"data updated"})
    
    def delete(self, request, po_id):

        """
        Delete a purchase order.

        Parameters:
        - po_id: The purchase order number

        Returns:
        - Response with success message
        """

        order =PurchaseOrder.objects.get(po_number = po_id)
        order.delete()
        return Response({"message":"data deleted"})
    

class VendorPerformanceView(APIView):

    """
    API endpoint for vendor performance operations.

    - GET: Retrieve vendor performance data
    """

    def get(self, request, po_id = None):

        """
        Retrieve vendor performance data.

        Parameters:
        - vendor_id: The vendor code

        Returns:
        - Response with vendor performance data
        """
        
        perform = PurchaseOrder.objects.get(vendor_code = po_id)
        perform1 = PurchaseOrderSerializer(perform)
        return Response(perform1.data)
