from modeltranslation.translator import TranslationOptions, register
from .models import UserProfile, Post, Comment


@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('bio',)

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text',)
