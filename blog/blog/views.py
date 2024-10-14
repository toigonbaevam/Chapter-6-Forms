from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    
class BlogDetailView(DetailView): 
    model = Post
    template_name = "post_detail.html"
class BlogCreateView(CreateView): 
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
    
class BlogUpdateView(UpdateView): 
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
class BlogDeleteView(DeleteView): 
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    
    
    


from django.shortcuts import render
from django.views import View

class PostCreateView(View):
    def get(self, request):
        return render(request, 'post_new.html') 

from .views import PostCreateView





 
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'post_list'  # This is used in your templates

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = 'post'  # This will be used in the post detail template

# You can add other views as needed, such as for creating or editing posts.



