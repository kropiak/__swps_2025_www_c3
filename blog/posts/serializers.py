from rest_framework import serializers
from .models import Topic, Category, Post


class TopicSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_lenght=60)
    created = serializers.DateTimeField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'topic', 'slug', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'updated_at']
