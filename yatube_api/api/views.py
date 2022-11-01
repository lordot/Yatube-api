from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.filters import SearchFilter

from posts.models import Post, Group, User
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from .serializers import *
from .permissions import IsAuthor


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthor, ]
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
    permission_classes = [IsAuthor, ]

    def get_post(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return post

    def get_queryset(self):
        post = self.get_post()
        queryset = post.comments.select_related('author')
        return queryset

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


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

    def create(self, request, *args, **kwargs,):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        following = User.objects.get(username=self.request.data['following'])
        if user.follower.filter(following=following).exists():
            return Response('Already following', status=HTTP_400_BAD_REQUEST)
        elif user == following:
            return Response('Same username', status=HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=HTTP_201_CREATED, headers=headers
        )
