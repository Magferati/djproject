from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def blog(request):
    return render(request, 'Blog.html', {'name': 'This is my blog content....'})

  

def show_items(request):
    blogs = Blog.objects.all()
    return render(request, 'items.html', {'blogs': blogs})

