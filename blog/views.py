from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from .forms import PostsForm

from django.db.models import F
def index(request):
    return render(request, 'blog/index.html', {'title': 'lists'})
def new_page(request):
    return render(request, 'blog/index2.html', {'title': 'tables'})
def css_page(request):
    return render(request, 'blog/index3.html', {'title': 'styles'})
def dartblog(request):
    return render(request, 'blog/index.html', {'title': 'dart'})
def pseudo(request):
    return render(request, 'blog/index4.html', {'title': 'pseudo'})
def forms(request):
    return render(request, 'blog/index5.html', {'title': 'forms'})
def adapt(request):
    return render(request, 'blog/index6.html', {'title': 'adapt'})
def get_category(request, slug):
    return render(request, 'blog/category.html', {'title': 'category'})
def get_post (request, slug):
    return render (request, 'blog/category.html')

class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['title']='Classic Blog Design'
        return context


class PostsByCategory (ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']=Category.objects.get(slug=self.kwargs['slug'])
        return context



class GetPost (DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views')+1
        self.object.save()
        self.object.refresh_from_db()
        return context

class PostsByTag(ListView):
    pass

def add_news(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = PostsForm()
    return render(request, 'blog/add_news.html', {'form':form})