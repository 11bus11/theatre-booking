from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('', views.PlayList.as_view(), name='plays'),
    path('', views.AboutTheatre.as_view(), name='about'),
    path('', views.Booking.as_view(), name='user'),
] 