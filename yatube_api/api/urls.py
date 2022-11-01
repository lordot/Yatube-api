from django.urls import path, include
from rest_framework import routers

from .views import PostsViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register('posts', PostsViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
