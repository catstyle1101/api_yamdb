from django.urls import path, include
from rest_framework import routers

from api.views.comments import CommentsViewSet

app_name = "api"
router_v1 = routers.DefaultRouter()
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentsViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]