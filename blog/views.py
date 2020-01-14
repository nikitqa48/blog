from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post/post_list.html'
    
def post_detail(request,pk):
    post= Post.objects.get(slug=pk)
    return render (request,'post/detail.html',{'post':post})

