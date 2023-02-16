from django_filters import rest_framework as filters

from api.filters import TitleFilter
from reviews.models.title import Title
from api.permissions import ReadOnly, IsAdmin
from api.serializers.titles_serializer import (TitlesSerializer,
                                               GetTitleSerializer)
from rest_framework import viewsets


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = GetTitleSerializer
    permission_classes = (IsAdmin | ReadOnly, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return TitlesSerializer
        return GetTitleSerializer
