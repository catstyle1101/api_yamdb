from api.views.categories import CategoryViewSet
from api.views.comment import CommentViewSet
from api.views.genres import GenreViewSet
from api.views.review import ReviewViewset
from api.views.titles import TitlesViewSet
from api.views.users import (
    GetConfirmationCodeView, GetTokenView, SignUpView, UserViewSet
)

__all__ = [
    CategoryViewSet, CommentViewSet, GenreViewSet, ReviewViewset,
    TitlesViewSet, UserViewSet, GetConfirmationCodeView,
    GetTokenView, SignUpView
]