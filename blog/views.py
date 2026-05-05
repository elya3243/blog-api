from rest_framework import generics, filters
from .serializers import PostSerializer, CommentSerializer, PostWriteSerializer, PostReadSerializer
from .models import Post, Comment, Like
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response


class PostListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'content']
    filterset_fields = ['author']
    queryset = Post.objects.select_related('author').prefetch_related('comments', 'likes')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostReadSerializer
        return PostWriteSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def get_queryset(self):
        return Post.objects.all()


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ToggleLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        like = Like.objects.filter(post=post, user=user).first()
        if like:
            like.delete()
            return Response({'message': 'unliked'})
        else:
            Like.objects.create(post=post, user=user)
            return Response({'message': 'liked'})
