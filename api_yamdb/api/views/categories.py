from django.shortcuts import get_object_or_404

from api.models.categories import Categories
from api.serializers.categories_serizlizer import CategorySerializer
from rest_framework import viewsets, filters, mixins


class ListCreateDeleteViewSet(mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    pass


class CategoryViewSet(ListCreateDeleteViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = False
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
