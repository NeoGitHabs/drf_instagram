from django.urls import path
from .views import UserProfileAPIView, FollowListAPIView, PostListAPIView, PostLikeListAPIView, CommentListAPIView, CommentLikeListAPIView, StoryListAPIView, SaveListAPIView, SaveItemListAPIView


urlpatterns = [
    path('user/<int:pk>/', UserProfileAPIView.as_view(), name='users'),
    path('follow/', FollowListAPIView.as_view(), name='follow_lists'),
    path('post_list/', PostListAPIView.as_view(), name='post_lists'),
    path('post_like_list/', PostLikeListAPIView.as_view(), name='post_like_list'),
    path('comment_list/', CommentListAPIView.as_view(), name='comment_lists'),
    path('comment_like_list/', CommentListAPIView.as_view(), name='comment_like_lists'),
    path('story_list/', StoryListAPIView.as_view(), name='story_lists'),
    path('save_list/', SaveListAPIView.as_view(), name='save_lists'),
    path('save_item_list/', SaveItemListAPIView.as_view(), name='save_item_lists'),
    ]
