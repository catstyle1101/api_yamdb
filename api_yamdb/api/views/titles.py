from api.models.titles import Titles
from api.serializers.titles_serializer import (TitlesSerializer,
                                               GetTitleSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    #permission_classes = False
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category__slug', 'genre__slug', 'name', 'year')

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return GetTitleSerializer
        return TitlesSerializer
