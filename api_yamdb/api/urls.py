from django.urls import path, include
from rest_framework import routers

from api.views.comment import CommentViewSet
from api.views.review import ReviewViewset

app_name = "api"
router_v1 = routers.DefaultRouter()
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename='comments',
)
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews",
    ReviewViewset,
    basename='reviews',
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
