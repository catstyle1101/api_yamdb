from reviews.models.genres import Genre
from api.permissions import ReadOnly, IsAdmin
from api.serializers.titles_serializer import GenreSerializer
from rest_framework import viewsets, filters, mixins


class ListCreateDeleteViewSet(mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    pass


class GenreViewSet(ListCreateDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdmin | ReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
