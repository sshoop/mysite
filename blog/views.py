from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Article, Category, Tag
from django.views.generic import ListView, DetailView, FormView
from .forms import CommentForm, SearchForm
import markdown2

# Create your views here.


def home(request):
    """
        主页视图

    """
    return render(request, 'home.html')


class IndexView(ListView):
    """
        博客首页视图 展示文章列表  继承ListView
    """
    template_name = 'blog/blog_index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        # 获取数据库中非草稿的数据
        article_list = Article.objects.filter(article_index='True', article_status='p').order_by('-article_change_time')

        for article in article_list:
            article.article_abstract = markdown2.markdown(article.article_abstract)

        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
        kwargs['tag_list'] = Tag.objects.all().order_by('tag_name')
        kwargs['date_archive'] = Article.objects.archive()
        kwargs['SearchForm'] = SearchForm()
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    """
        文章细节视图
    """
    model = Article
    template_name = 'blog/blog_detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        # 将正文转化为html文本 便于在网页上显示
        obj.article_text = markdown2.markdown(obj.article_text, extras=['fenced-code-blocks'])
        return obj

    def get_context_data(self, **kwargs):
        # 返回额外的数据 评论列表 评论表单
        kwargs['comment_list'] = self.object.comment_set.all()
        kwargs['form'] = CommentForm()
        return super(ArticleDetailView, self).get_context_data(**kwargs)


class ArchiveView(ListView):
    """
        博客Archive视图 以时间先后顺序展示文章列表  继承ListView
    """
    template_name = 'blog/blog_archive.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        # 获取数据库中非草稿的数据
        article_list = Article.objects.filter(article_status='p').order_by('-article_create_time')
        """for article in article_list:
            if article.article_change_time.month < 10:
                article.article_change_time.month = """
        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
        kwargs['tag_list'] = Tag.objects.all().order_by('tag_name')
        kwargs['date_archive'] = Article.objects.archive()
        kwargs['SearchForm'] = SearchForm()
        return super(ArchiveView, self).get_context_data(**kwargs)


class CategoryView(ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(article_category=self.kwargs['category_id'], article_status='p')
        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
        kwargs['tag_list'] = Tag.objects.all().order_by('tag_name')
        return super(CategoryView, self).get_context_data(**kwargs)


class CommentPostView(FormView):
    form_class = CommentForm
    template_name = 'blog/blog_detail.html'

    def form_valid(self, form):
        target_article = get_object_or_404(Article, pk=self.kwargs['article_id'])
        comment = form.save(commit=False)
        comment.comment_article = target_article
        comment.save()

        self.success_url = target_article.get_absolute_url()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        target_article = get_object_or_404(Article, pk=self.kearges['article_id'])
        return reverse(self.request, 'blog/blog_detail.html', {
            'form': form,
            'article': target_article,
            'comment_list': target_article.comment_set.all()
        })


class TagView(ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        """
            根据标签检索出该标签下的文章

        """
        article_list = Article.objects.filter(article_tag=self.kwargs['tag_id'], article_status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('tag_name')
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
        # kwargs['date_archive'] = Article.objects.archive()
        return super(TagView, self).get_context_data(**kwargs)


class DateView(ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        article_list = Article.objects.filter(article_create_time__year=year, article_create_time__month=month)
        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
        # kwargs['tag_list'] = Tag.objects.all().order_by('tag_name')
        kwargs['date_archive'] = Article.objects.archive()
        # kwargs['span_list'] = ['default', 'primary', 'success', 'info', 'warning', 'danger']
        return super(DateView, self).get_context_data(**kwargs)


def SearchView(request):
    search_name = request.GET['search_name']
    article_list = Article.objects.filter(article_title__contains=search_name)
    return render(request, 'blog/blog_index.html', {'article_list': article_list})


def AboutView(request):
    """
        AoutMe（简历）视图
    :param request:
    :return:
    """
    return render(request, 'about.html')







