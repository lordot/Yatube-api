from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.filters import SearchFilter

from posts.models import Post, Group

from .serializers import PostSerializer, CommentSerializer
from .serializers import FollowSerializer, GroupSerializer
from .permissions import IsAuthorOrReadOnly


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author', 'group')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_post(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return post

    def get_queryset(self):
        return self.get_post().comments.select_related('author')

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )


class FollowViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['following__username', ]

    def get_queryset(self):
        user = self.request.user
        queryset = user.follower.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
