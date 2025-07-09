from rest_framework import serializers
from .models import UserProfile, Follow, Post, PostLike, Comment, CommentLike, Story, Save, SaveItem
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
# ------------------------------------------------------------

class UserProfileSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(format='%d-%m-%Y')
    email = serializers.EmailField(validators=[UniqueValidator(queryset=UserProfile.objects.all())])
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'user_age', 'bio', 'image', 'website', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=UserProfile.objects.all())])
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'user_age', 'bio', 'image', 'website']
        extra_kwargs = {'password': {'write_only': True}}

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['follower', 'following', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'image', 'video', 'description', 'hashtag', 'created_at']

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['user', 'post', 'like', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', 'parent', 'created_at']

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['user', 'comment', 'like', 'created_at']

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['user', 'image', 'video', 'created_at']

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = ['user']

class SaveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveItem
        fields = ['post', 'save', 'created_date']
