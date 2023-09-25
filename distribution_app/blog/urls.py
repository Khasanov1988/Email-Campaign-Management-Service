from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    # URL pattern for creating a new post
    path('create/', PostCreateView.as_view(), name='create'),

    # URL pattern for listing posts with a 60-second cache timeout
    path('', cache_page(60)(PostListView.as_view()), name='list'),

    # URL pattern for viewing a single post
    path('view/<int:pk>/', PostDetailView.as_view(), name='view'),

    # URL pattern for editing an existing post
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),

    # URL pattern for deleting an existing post
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]
