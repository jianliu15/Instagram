# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from Insta.forms import CustomUserCreationForm

from Insta.models import Post

# Create your views here.

class HelloWorld(TemplateView):
    template_name = 'test.html'

# Create CRUD
# Read
class PostListView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# Create
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    fields = '__all__'
    login_url = 'login'

# Update
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']

# Delete
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')

# Create Signup View
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")