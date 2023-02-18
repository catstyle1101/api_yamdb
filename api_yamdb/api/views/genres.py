from rest_framework import filters

from api.mixins import ListCreateDeleteViewSet
from api.permissions import IsAdmin, ReadOnly
from api.serializers import GenreSerializer
from reviews.models.genres import Genre


class GenreViewSet(ListCreateDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdmin | ReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
