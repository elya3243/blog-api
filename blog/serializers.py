from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already exists')
        return value

    def validate_password(self, value):
        if len(value['password']) < 8:
            raise serializers.ValidationError({'password': 'Password must be at least 8 characters'})
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(read_only=True, many=True)

    def get_likes_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_author(self, obj):
        return {
            'username': obj.author.username,
            'id': obj.author.id
        }

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return obj.likes.count()


class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def create(self, validated_data):
        return Post.objects.create(author=self.context['request'].user, **validated_data)
