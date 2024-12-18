from rest_framework import serializers
from users.api.serializers import UserSerializer
from posts.models import Post
from categories.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug','miniature','created','published' ,'user','category' ]
