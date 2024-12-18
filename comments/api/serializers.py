from rest_framework import serializers
from users.api.serializers import UserSerializer
from posts.api.serializers import PostSerializer
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    #post = PostSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id','content','created','user','post']