from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
       
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post

