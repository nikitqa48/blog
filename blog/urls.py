from django.urls import path
from blog.views import *
from django.conf.urls import include

urlpatterns = [
    path('post',PostListView.as_view(),name="post_list"),
    path('detail/<slug:pk>',post_detail, name='post_detail'),
    path('share/', post_share, name='post_share')

]

