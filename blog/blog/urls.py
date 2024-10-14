from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    )
urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
     path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("", BlogListView.as_view(), name="home"),
    ]




# blog/urls.py
from django.urls import path
from .views import BlogListView, PostCreateView  

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),  
]



from django.urls import path
from .views import HomePageView, PostDetailView  # Ensure the views are imported

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Home page URL pattern
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Detail view URL pattern
    # Add any other URL patterns as needed
]



from django.urls import path
from .views import HomePageView, PostDetailView, PostCreateView  # Ensure the PostCreateView is imported

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Home page
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Post detail page
    path('post/new/', PostCreateView.as_view(), name='post_new'),  # New post creation page
    # Add other URL patterns as needed
]

