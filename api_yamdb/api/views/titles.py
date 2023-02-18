from django_filters import rest_framework as filters
from rest_framework import viewsets

from api.filters import TitleFilter
from api.permissions import IsAdmin, ReadOnly
from api.serializers import GetTitleSerializer, TitlesSerializer
from reviews.models import Title


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
