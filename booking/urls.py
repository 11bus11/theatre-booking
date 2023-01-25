from . import views
from django.urls import path


urlpatterns = [
    path('dates/<int:play_id>/', views.play_dates, name='booking_date'),
    path('form/<int:nowplaying_id>/', views.place_booking, name='booking_form'),
    path('', views.plays, name='plays'),
    path('add/', views.add_play, name='add_play'),
    path('edit/<int:play_id>/', views.edit_play, name='edit_play'),
    path('delete/<int:play_id>/', views.delete_play, name='delete_play'),
    path('all-bookings/', views.all_bookings, name='all_bookings'),
] 