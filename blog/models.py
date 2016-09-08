from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(u'类名', max_length=20)
    category_create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    category_change_time = models.DateTimeField(u'修改时间', auto_now=True)

    def __str__(self):
        return self.category_name


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发布'),
    )

    article_title = models.CharField(u'标题', max_length=50)
    article_text = models.TextField(u'正文', help_text='支持MarkDown语法')
    article_abstract = models.TextField(u'摘要', help_text='支持MarkDown语法')
    article_create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    article_change_time = models.DateTimeField(u'修改时间', auto_now=True)
    article_status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    article_index = models.BooleanField(u'首页', default=False)
    article_views = models.PositiveIntegerField(u'浏览量', default=0)
    article_likes = models.PositiveIntegerField(u'点赞数', default=0)
    article_category = models.ForeignKey('Category', verbose_name='分类')
    article_tag = models.ManyToManyField('Tag', verbose_name='标签', blank=True,)

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_id': self.pk})


class Comment(models.Model):
    comment_name = models.CharField(u'昵称', max_length=20)
    comment_text = models.CharField(u'评论内容', max_length=256)
    comment_create_time = models.DateTimeField(u'发表时间', auto_now_add=True)
    comment_article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text[:20]


class Tag(models.Model):
    tag_name = models.CharField(u'标签名', max_length=20)
    tag_create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    tag_change_time = models.DateTimeField(u'修改时间', auto_now=True)

    def __str__(self):
        return self.tag_name



