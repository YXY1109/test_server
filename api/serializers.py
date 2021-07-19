# -*-coding:utf-8-*-

from rest_framework import serializers
from .models import Banner, User


# banner列表
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


# 用户
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
