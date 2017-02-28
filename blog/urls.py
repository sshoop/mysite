from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<category_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentPostView.as_view(), name='comment'),
    url(r'^tag/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^date/(?P<year>\d+)/(?P<month>\d+)$', views.DateView.as_view(), name='date'),
    url(r'^search/$', views.SearchView, name='search'),
    url(r'^test/$', views.ArchiveView.as_view(), name='archive'),

]