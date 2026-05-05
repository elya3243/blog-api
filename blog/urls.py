from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView, ToggleLikeView

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('posts/<int:pk>/like/', ToggleLikeView.as_view()),
]