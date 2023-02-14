from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views.titles import TitlesViewSet
from api.views.genres import GenreViewSet
from api.views.categories import CategoryViewSet

router = DefaultRouter()
router.register('titles', viewset=TitlesViewSet)
router.register('genres', viewset=GenreViewSet)
router.register('categories', viewset=CategoryViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]