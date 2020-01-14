from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
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

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title