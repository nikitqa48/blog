from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import *


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post/post_list.html'
    
def post_detail(request,pk):
    post= Post.objects.get(slug=pk)
    return render (request,'post/detail.html',{'post':post})

def post_share(request,upk):
    print(post_id)
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == "POST":
        form = EmailPostForm
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = format(cd['name'], cd['email'], post.title)
            message = format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'post/share.html',{'post':post,
                                                'form':form,
                                                "sent":sent})