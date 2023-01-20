from . import views
from django.urls import path


urlpatterns = [
    path('form/', views.Booking, name='booking'),
    path('', views.play_showings, name='plays'),
] 