from rest_framework import filters

from api.mixins import ListCreateDeleteViewSet
from api.permissions import IsAdmin, ReadOnly
from api.serializers import CategorySerializer
from reviews.models import Categories


class CategoryViewSet(ListCreateDeleteViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdmin | ReadOnly, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
