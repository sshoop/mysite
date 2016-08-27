from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Article, Category
from django.views.generic import ListView, DetailView, FormView
from .forms import CommentForm
import markdown2
# Create your views here.


def home(request):
    return render(request, 'home.html')


class IndexView(ListView):
    """
        博客首页视图 展示文章列表
    """
    template_name = 'blog/blog_index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        # 获取数据库中非草稿的数据
        article_list = Article.objects.filter(article_index='True')
        '''
        for article in article_list:
            article.body = markdown2.markdown(article)
        '''
        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/blog_detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        # 将正文转化为html文本 便于在网页上显示
        obj.article_text = markdown2.markdown(obj.article_text)
        return obj

    def get_context_data(self, **kwargs):
        kwargs['comment_list'] = self.object.comment_set.all()
        kwargs['form'] = CommentForm()
        return super(ArticleDetailView, self).get_context_data(**kwargs)


class CategoryView(ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(article_category=self.kwargs['category_id'], article_status='p')
        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
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
        target_article = get_object_or_404(Article, pk=self.kwarges['article_id'])
        return reverse(self.request, 'blog/blog_detail.html', {
            'form': form,
            'article': target_article,
            'comment_list': target_article.comment_set.all()
        })






