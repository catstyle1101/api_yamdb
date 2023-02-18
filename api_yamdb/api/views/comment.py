from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.permissions import IsAdmin, IsAuthorOrReadOnly, IsModerator
from api.serializers import CommentSerializer
from reviews.models import Review


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAdmin | IsModerator | IsAuthorOrReadOnly, )

    def get_review(self):
        return get_object_or_404(Review, pk=self.kwargs.get('review_id'))

    def get_queryset(self):
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())
