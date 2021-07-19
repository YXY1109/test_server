from django.db import models
from django.utils.html import format_html

from TestServer.base.choices import BANNER_LIST, STATUS_LIST


# 用户
class User(models.Model):
    id = models.AutoField(primary_key=True)
    secret = models.CharField(unique=True, max_length=255)
    username = models.CharField(max_length=128, blank=True, null=True, verbose_name='用户名')
    avatar = models.CharField(max_length=255, blank=True, null=True, verbose_name='用户头像')

    def image_data(self):
        if self.avatar:
            return format_html(
                '<img src="{}" width="100px"/>',
                self.avatar,
            )
        else:
            return '无效图片'

    class Meta:
        ordering = ['id']
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name


# 轮播
class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    action = models.IntegerField(default=101, choices=BANNER_LIST)
    status = models.IntegerField(default=1, choices=STATUS_LIST)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True)

    def image_data(self):
        if self.url:
            return format_html(
                '<img src="{}" width="100px"/>',
                self.url,
            )
        else:
            return '无效图片'

    class Meta:
        ordering = ['id']
        verbose_name = '轮播列表'
        verbose_name_plural = verbose_name
