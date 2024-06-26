from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view() , name='sandbox-home'),
    path('about/', views.about, name="sandbox-about"),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='post-delete'),
     path('post/new/', PostCreateView.as_view(), name = 'post-create'),
]