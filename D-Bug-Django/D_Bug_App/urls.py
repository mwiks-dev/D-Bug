from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)