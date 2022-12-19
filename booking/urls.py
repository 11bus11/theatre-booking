from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('/plays', views.PlayList.as_view(), name='plays'),
    path('/about', views.AboutTheatre.as_view(), name='about'),
    path('/user', views.Booking.as_view(), name='user'),
] 