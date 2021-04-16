from . import views
from django.urls import path
from blog.sitemaps import PostSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "posts": PostSitemap,
}


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]