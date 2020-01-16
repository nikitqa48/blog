from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        post = Post.objects.filter(status='published')
        return post
   
    def lastmod(self, obj):
        return obj.publish