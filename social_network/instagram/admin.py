from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import UserProfile, Follow, Post, PostLike, Comment, CommentLike, Story, Save, SaveItem
from .translation import UserProfileTranslationOptions, PostTranslationOptions, CommentTranslationOptions


admin.site.register(Follow)
admin.site.register(PostLike)
admin.site.register(CommentLike)
admin.site.register(Story)
admin.site.register(Save)
admin.site.register(SaveItem)

@admin.register(UserProfile, Post, Comment)
class TranslateAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
