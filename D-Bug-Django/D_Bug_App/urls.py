from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]