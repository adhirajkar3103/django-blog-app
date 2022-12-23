from django.urls import path,include
from .views import BlogListView,BlogView,CreateBlogView
urlpatterns = [
    path('post/new/',CreateBlogView.as_view(),name='post_new'),
    path('post/<int:pk>/',BlogView.as_view(),name='blog_detail'),
    path('',BlogListView.as_view(),name='all_blogs'),
]