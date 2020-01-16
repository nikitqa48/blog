from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import *
from django.core.mail import send_mail



class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'post/post_list.html'
    

def post_detail(request,pk):
    post= Post.objects.get(slug=pk)
    comments = Comment.objects.filter(active=True, post=post)
    form = CommentForm()
    context={
        'post':post,
        'comments':comments,
        'form':form
    }
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            context={
                'new_comment':new_comment,
                'form':form
            }
    return render (request,'post/detail.html',context)


def post_share(request,pk):
    """Отправка сообщений на почту"""

    sent = False
    if request.method == "GET":
        form = EmailPostForm()
        post = Post.objects.get(slug=pk)
        context = {
            'post':post,
            'form':form,
            'sent':sent
        }
    else:
        form = EmailPostForm(request.POST)
        post = Post.objects.get(slug=pk)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            """Отправка урла на почту с помощью метода reverse модели Post(В аргументах метода отправляется ключ)"""

            subject = '{} Реккомендует к чтению'.format(cd['name'], cd['email'], post.title)
            comments = form['comments'].value()
            message = 'Прочитай' + ' ' +post.title+ " "+ "от"+ ' '+cd['name']+' '+comments + " " + post_url
            send_mail(subject, message, 'nikitqaa1901@gmail.com', [cd['to']])
            sent = True
        else:
            form = EmailPostForm()
        context = {
            'post':post,
            'form':form,
            'sent':sent
        }
    return render(request, 'post/share.html', context)

