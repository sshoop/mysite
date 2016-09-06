from django.contrib import admin
from .models import Article, Category, Comment, Tag


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 显示的字段
    fieldsets = (
        ('文章主题', {
            'fields': ('article_title', 'article_text', 'article_abstract', 'article_category', 'article_tag')
        }),
        ('其它设置', {
            'fields': (('article_views', 'article_likes',), ('article_status', 'article_index')),

        })
    )
    # 查询字段
    list_filter = ('article_create_time', 'article_index', 'article_status')
    search_fields = ('article_title',)
    # actions

    def make_not_index(self, request, queryset):
        queryset.update(article_index=False)
    make_not_index.short_description = 'Make selected article as not index'

    def make_index(self, request, queryset):
        row_update = queryset.update(article_index=True)
        if row_update == 1:
            message_bit = '1 article was'
        else:
            message_bit = '%s articles was' % row_update
        self.message_user(request, '%s successfully marked as index.' % message_bit)
    make_index.short_description = 'Make selected article as index'

    def make_published(self, request, queryset):
        row_update = queryset.update(article_status='p')
        if row_update == 1:
            message_bit = '1 article was'
        else:
            message_bit = '%s articles was' % row_update
        self.message_user(request, '%s successfully marked as published.' % message_bit)
    make_published.short_description = 'Make selected article as published'

    def make_draft(self, request, queryset):
        queryset.update(article_status='d')
    make_draft.short_description = 'Make selected article as draft'

    actions = ['make_index', 'make_not_index', 'make_published', 'make_draft']


class CategoryAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)