from . import views
from django.urls import path

urlpatterns = [
    path('', views.PlayList.as_view(), name='home'),
]