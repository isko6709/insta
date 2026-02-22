from modeltranslation.translator import register, TranslationOptions
from .models import Post, Comment, Hashtag


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Hashtag)
class HashtagTranslationOptions(TranslationOptions):
    fields = ('hashtag_name',)