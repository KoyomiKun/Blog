from django.db import models
from blogadmin.models import Post


# Create your models here.

class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'deleted')
    )
    target = models.ForeignKey(Post, verbose_name='target')
    content = models.CharField(max_length=2000, verbose_name='comment')
    nickname = models.CharField(max_length=50, verbose_name='nickname')
    website = models.URLField(verbose_name='website')
    email = models.EmailField(verbose_name='email')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='status')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create_time')

    class Meta:
        verbose_name = verbose_name_plural = 'comment'
