from django.urls import path, include
from rest_framework import routers

from api.views.categories import CategoryViewSet
from api.views.comment import CommentViewSet
from api.views.genres import GenreViewSet
from api.views.titles import TitlesViewSet
from api.views.review import ReviewViewset
from api.views.users import UserSingupView, UserGetTokenView

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
router_v1.register('titles', TitlesViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', UserSingupView.as_view()),
    path('v1/auth/token/', UserGetTokenView.as_view()),
]
