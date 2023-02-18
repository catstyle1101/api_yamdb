from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.permissions import IsAdmin, IsAuthorOrReadOnly, IsModerator
from api.serializers import ReviewSerializer
from reviews.models import Title


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAdmin | IsModerator | IsAuthorOrReadOnly, )

    def get_title_object(self):
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Title, id=title_id)

    def get_queryset(self):
        title = self.get_title_object()
        return title.reviews.all()

    def perform_create(self, serializer):
        title = self.get_title_object()
        serializer.save(author=self.request.user, title=title)
