from django.views.generic import ListView,DetailView,CreateView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class CreateBlogView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','body']
