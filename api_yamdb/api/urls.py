from django.urls import path, include
from rest_framework import routers

from api.views.categories import CategoryViewSet
from api.views.comment import CommentViewSet
from api.views.genres import GenreViewSet
from api.views.titles import TitlesViewSet
from api.views.review import ReviewViewset
from api.views.users import (
    GetConfirmationCodeView, SignUpView, GetTokenView, UserViewSet
)

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
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/code/', GetConfirmationCodeView.as_view(),
         name='get_confirmation_code'),
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', GetTokenView.as_view(), name='login'),
]
