from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'deleted')
    )

    name = models.CharField(max_length=50, verbose_name='name')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    is_nav = models.BooleanField(default=False, verbose_name='is_nav')
    owner = models.ForeignKey(User, verbose_name='author')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create_time')

    class Meta:
        verbose_name = verbose_name_plural = 'Category'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'deleted')
    )
    name = models.CharField(max_length=10, verbose_name='name')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    owner = models.ForeignKey(User, verbose_name='author')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create_time')

    class Meta:
        verbose_name = verbose_name_plural = 'Tag'


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'deleted'),
        (STATUS_DRAFT, 'draft')
    )
    name = models.CharField(max_length=255, verbose_name='name')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='description')
    content = models.TextField(verbose_name='content', help_text='.md')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    category = models.ForeignKey(Category, verbose_name='category')
    tag = models.ForeignKey(Tag, verbose_name='tag')
    owner = models.ForeignKey(User, verbose_name='author')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create_time')

    class Meta:
        verbose_name = verbose_name_plural = 'Post'
        ordering = ['-id']
