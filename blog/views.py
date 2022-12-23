from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
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

class UpdateBlogView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('all_blogs')