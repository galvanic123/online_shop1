from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('blog/home/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/home/', BlogListView.as_view(), name='home'),
    path('blog/create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/home/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/home/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete')
]
