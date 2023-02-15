from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.models import Review, Titles
from api.serializers.review_serializer import ReviewSerializer


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_review(self):
        return get_object_or_404(Titles, pk=self.kwargs.get("title_id"))

    def get_queryset(self):
        return self.get_review().review.all()
