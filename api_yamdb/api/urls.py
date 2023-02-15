from django.urls import include, path

from api.views import UserViewSet, UserSignupView, UserGetTokenView

urlpatterns = [
    path('v1/auth/signup/', UserSignupView.as_view()),
    path('v1/auth/token/', UserGetTokenView.as_view())
]
