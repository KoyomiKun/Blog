from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'deleted')
    )
    title = models.CharField(max_length=50, verbose_name='title')
    href = models.URLField(verbose_name='link')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name='weight',
                                         help_text='Rank by weight')
    owner = models.ForeignKey(User, verbose_name='author')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create_time')

    class Meta:
        verbose_name = verbose_name_plural = 'link'


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, 'show'),
        (STATUS_HIDE, 'hide')
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, 'NEWS'),
        (3, 'HOTS'),
        (4, 'HOTS COMMENT')
    )
    title = models.CharField(max_length=50, verbose_name='title')
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name='display')
    content = models.CharField(max_length=500, blank=True, verbose_name='content',
                               help_text='if not HTML,empty is available.')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='status')
    owner = models.ForeignKey(User, verbose_name='author')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create_time')

    class Meta:
        verbose_name_plural = verbose_name = 'sidebar'


