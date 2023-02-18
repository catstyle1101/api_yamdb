from rest_framework import mixins, viewsets


class ListCreateDeleteViewSet(
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    pass
