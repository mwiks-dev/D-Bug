from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('profile/',views.ProfileFunc,name='profile'),
    path('profile/<str:name>/',views.ProfileDetails,name="Profile_details")
]