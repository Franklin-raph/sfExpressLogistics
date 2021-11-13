from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('packageTracking/', views.packageTracking, name="packageTracking"),
    path('contact/', views.contact, name="contact"),
    path('receipt/<str:tracking_id>', views.receipt, name="receipt"),
    path('trackinInfo/<str:track_id>', views.trackinInfo, name="trackinInfo"),
    # path('update/', views.updateTask, name="update")
] 