from django.urls import path,include
from .views import BlogListView,BlogView
urlpatterns = [
    path('post/<int:pk>/',BlogView.as_view(),name='blog_detail'),
    path('',BlogListView.as_view(),name='all_blogs'),
]