from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    tags = TaggableManager()
    STATUS_CHOISES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликован')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок',max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', null='true')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField("Текст")
    publish = models.DateTimeField("Опубликован",default=timezone.now)
    created = models.DateTimeField("Создан",auto_now_add=True)
    updated = models.DateTimeField("Обновлен",auto_now=True)
    status = models.CharField("Статус",max_length=10,choices=STATUS_CHOISES, default='draft')

    def get_absolute_url(self):
        return reverse('post_detail',
                        args=[self.slug])
    
    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='Пост', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=25)
    email = models.EmailField('Почта')
    body = models.TextField('Текст')
    created = models.DateTimeField('Создан',auto_now_add=True)
    update = models.DateTimeField('Обновлен',auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
    
    def __str__(self):
        return 'Комментарий от' + " "+self.name + " "+ self.post.title