from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)