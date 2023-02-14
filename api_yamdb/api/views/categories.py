from api.models.categories import Categories
from api.serializers.categories import CategorySerializer
from rest_framework import viewsets, filters, mixins


class ListCreateDeleteViewSet(mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    pass


class CategoryViewSet(ListCreateDeleteViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = False
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
