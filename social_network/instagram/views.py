from rest_framework import generics, viewsets
from .models import UserProfile, Follow, Post, PostLike, Comment, CommentLike, Story, Save, SaveItem
from .serializers import UserProfileSerializer, UserProfileCreateSerializer, FollowSerializer, PostSerializer, PostLikeSerializer, CommentSerializer, CommentLikeSerializer, StorySerializer, SaveSerializer, SaveItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions


class UserProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

    # permission_classes = [permissions.IsAuthenticated]

class UserProfileCreteAPIView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCreateSerializer

class FollowListAPIView(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    # permission_classes = [permissions.IsAuthenticated]

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['hashtag']
    search_fields = ['username']
    ordering_fields = ['created_at']
    ordering = ['created_at']

class PostLikeListAPIView(generics.ListAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

    # permission_classes = [permissions.IsAuthenticated]

class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # permission_classes = [permissions.IsAuthenticated]

class CommentLikeListAPIView(generics.ListAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer

    # permission_classes = [permissions.IsAuthenticated]

class StoryListAPIView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    # permission_classes = [permissions.IsAuthenticated]

class SaveListAPIView(generics.ListAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer

    # permission_classes = [permissions.IsAuthenticated]

class SaveItemListAPIView(generics.ListAPIView):
    queryset = SaveItem.objects.all()
    serializer_class = SaveItemSerializer
