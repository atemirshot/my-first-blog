from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title')
