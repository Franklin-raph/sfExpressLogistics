from django.contrib import admin
from .models import Receipt
from .models import Packages
from .models import TrackingInfo
from .models import TrackingRoute

admin.site.register(Receipt)
admin.site.register(Packages)
admin.site.register(TrackingInfo)
admin.site.register(TrackingRoute)

# Register your models here.
