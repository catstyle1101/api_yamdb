from django.urls import path, include
from rest_framework import routers

from api.views.titles import TitlesViewSet
from api.views.genres import GenreViewSet
from api.views.categories import CategoryViewSet

app_name = "api"
router_v1 = routers.DefaultRouter()
#router_v1.register(
#    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
#    CommentsViewSet,
#    basename='comments'
#)
router_v1.register('titles', viewset=TitlesViewSet)
router_v1.register('genres', viewset=GenreViewSet)
router_v1.register('categories', viewset=CategoryViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
