from . import views
from django.urls import path


urlpatterns = [
    path('', views.NowPlaying, name='plays'),
    path('booking/', views.Booking, name='booking'),
] 