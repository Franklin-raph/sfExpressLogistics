from django.shortcuts import render
from django.http import HttpResponse
from .models import Packages
from .models import Receipt
from .models import TrackingRoute
from .models import TrackingInfo

def error_404_page(request, exception):
    return render(request, '404.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def packageTracking(request):
    # if request.method == 'POST':
    #     tracking_id = request.POST.get('tracking_id')
    #     result = TrackingInfo.objects.filter(order_id=tracking_id)
    #     print("This is the result")
    #     print(result)
    #     print("The result is up")
    
    return render(request, 'packageTracking.html')

def contact(request):
    return render(request, 'contact.html')

def receipt(request, tracking_id):
    receipt_details = Receipt.objects.get(order_id = tracking_id)
    package_table = Packages.objects.filter(tracking_details = receipt_details)
    sub_total = 0
    for package in package_table:
        sub_total += (package.price * package.quantity)
    total = 0
    total += sub_total + receipt_details.shipment_insurance
    return render(request, 'receipt.html', {'receipt_details':receipt_details, 'package_table':package_table, 'sub_total':sub_total, 'total':total})


def trackinInfo(request, track_id):
    tracking_info = TrackingInfo.objects.get(order_id = track_id)
    tracking_route = TrackingRoute.objects.filter(additional_info = tracking_info)
    
    return render(request, 'trackinInfo.html', {'tracking_info':tracking_info, 'tracking_route':tracking_route})

