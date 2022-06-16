from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)