from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

posts = [
	{
	"author":"Abhi",
	"title":"Abhi's blog post",
	"content":"my first post content",
	"date_posted":"06-05-2024"
	},
	{
	"author":"Abhi",
	"title":"Abhi's blog post",
	"content":"second post content",
	"date_posted":"06-05-2024"
	},
]


def home(request):
    context = {
        'posts': Post.objects.all()
	}
    return render (request, 'sandbox/home.html', context )

def about(request):
    return render (request, 'sandbox/about.html', {'title':"About"})

class PostListView(ListView):
    model = Post
    template_name = 'sandbox/home.html'
    # <app>/<model>_<view_type>
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False
