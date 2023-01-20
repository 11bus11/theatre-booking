from . import views
from django.urls import path


urlpatterns = [
    path('dates/<int:play_id>/', views.play_dates, name='booking_date'),
    #path('form/', views.Booking, name='booking_form'),
    path('', views.play_showings, name='plays'),
    path('add/', views.add_play, name='add_plays'),
    #path('edit/<int:play_id>/', views.edit_play, name='edit_plays'),
    #path('delete/<int:play_id>/', views.delete_play, name='delete_plays'),
] 