from django.db import models

# Create your models here.
class Receipt (models.Model):
    receipt_date = models.DateTimeField()
    from_name = models.CharField(max_length=200)
    from_phone = models.CharField(max_length=200)
    from_adress = models.CharField(max_length=200)
    from_office = models.CharField(max_length=200)

    to_name = models.CharField(max_length=200)
    to_phone = models.CharField(max_length=200)
    to_adress = models.CharField(max_length=200)
    to_office = models.CharField(max_length=200)

    order_id = models.CharField(max_length=200)
    payment_due = models.DateTimeField()
    booking_mode = models.CharField(max_length=200)
    shipment_insurance = models.IntegerField()

class Packages (models.Model):
    quantity = models.IntegerField()
    product = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    tracking_details = models.ForeignKey(Receipt, on_delete = models.CASCADE, related_name = 'packages')

class TrackingInfo (models.Model):
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    services = models.CharField(max_length=200)
    goods_type = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    pickup_date_time = models.DateTimeField()
    description = models.CharField(max_length=200)

    consignee_name = models.CharField(max_length=200)
    consignee_phone = models.CharField(max_length=200)
    consignee_address = models.CharField(max_length=200)

    shipper_name = models.CharField(max_length=200)
    shipper_address = models.CharField(max_length=200)

    order_id = models.CharField(max_length=200)
    current_status = models.CharField(max_length=200)
    booking_mode = models.CharField(max_length=200)

class TrackingRoute (models.Model):
    freight = models.CharField(max_length=200)
    last_location = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    additional_info = models.ForeignKey(TrackingInfo, on_delete = models.CASCADE, related_name = 'packages')

    
    

