from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count
from django.db.models import Avg
from django.db.models import F
from django.db import models
from django.utils import timezone
# Create your models here.

class Vendor(models.Model):
    # Vendor's name
    name = models.CharField(max_length=200)   

    # Contact information of the vendor  
    contact_details = models.TextField()   

    # Physical address of the vendor
    address = models.TextField()    

    # A unique identifier for the vendor
    vendor_code = models.CharField(max_length=50, unique=True, primary_key=True)      

    # Tracks the percentage of on-time deliveries
    on_time_delivery_rate = models.FloatField(default=0) 

    # Average rating of quality based on purchase
    quality_rating_avg = models.FloatField(default=0)

    # Average time taken to acknowledge purchase orders
    average_response_time = models.FloatField(default=0)

    # Percentage of purchase orders fulfilled successfully
    fulfillment_rate = models.FloatField(default=0)


class PurchaseOrder(models.Model):
    # Unique number identifying the PO(Purchase order)
    po_number = models.CharField(max_length=50, unique=True, primary_key=True)
    
    # Link to the Vendor model
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
    # Date when the order was placed
    order_date = models.DateTimeField()
    
    # Expected or actual delivery date of the order
    delivery_date = models.DateTimeField(null=True, blank=True)
    
    #data of the delivered data
    delivered_data = models.DateTimeField(null=True, blank=True)

    # Details of items ordered (stored as JSON)
    items = models.JSONField()
    
    # Total quantity of items in the PO
    quantity = models.IntegerField()
    
    # Current status of the PO (e.g., pending, completed, canceled)
    status = models.CharField(max_length=20)
    
    # Rating given to the vendor for this PO (nullable)
    quality_rating = models.FloatField(null=True, blank=True)
    
    # Timestamp when the PO was issued to the vendor
    issue_date = models.DateTimeField()
    
    # Timestamp when the vendor acknowledged the PO (nullable)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)


class HistoricalPerformance(models.Model):
    # Link to the Vendor model
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
    # Date of the performance record
    date = models.DateTimeField()
    
    # Historical record of the on-time delivery rate
    on_time_delivery_rate = models.FloatField()
    
    # Historical record of the quality rating average
    quality_rating_avg = models.FloatField()
    
    # Historical record of the average response time
    average_response_time = models.FloatField()
    
    # Historical record of the fulfilment rate
    fulfillment_rate = models.FloatField()


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.delivered_data is None:
        instance.delivered_data = timezone.now()
        instance.save()

    # Update On-Time Delivery Rate
    completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
    on_time_deliveries = completed_orders.filter(delivery_date__gte=F('delivered_data'))
    on_time_delivery_rate = on_time_deliveries.count() / completed_orders.count()
    instance.vendor.on_time_delivery_rate = on_time_delivery_rate if on_time_delivery_rate else 0

    # Update Quality Rating Average
    completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
    quality_rating_avg = completed_orders_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
    instance.vendor.quality_rating_avg = quality_rating_avg if quality_rating_avg else 0
    instance.vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_response_time(sender, instance, **kwargs):
    # Update Response Time
    response_times = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
    average_response_time = sum((ack_date - issue_date ).total_seconds() for ack_date, issue_date in response_times)
    if average_response_time < 0:
        average_response_time = 0
    if response_times:
        average_response_time = average_response_time / len(response_times)
    else:
        average_response_time = 0
    instance.vendor.average_response_time = average_response_time
    instance.vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    # Update Fulfillment Rate
    fulfilled_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
    fulfillment_rate = fulfilled_orders.count() / PurchaseOrder.objects.filter(vendor=instance.vendor).count()
    instance.vendor.fulfillment_rate = fulfillment_rate
    instance.vendor.save()

