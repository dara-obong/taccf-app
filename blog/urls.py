from django.urls import path
from .import views as blog_views
from .views import (
    PostListView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    UserPostListView, 
    PostDetailView,
    HomeView, 
)

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('about/', blog_views.about, name='blog-about'),
    path('contact/', blog_views.contact, name='blog-contact'),
    path('posts/', PostListView.as_view(), name="blog-posts"),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', blog_views.add_comment, name='add-comment'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]