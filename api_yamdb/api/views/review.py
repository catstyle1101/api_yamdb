from rest_framework import viewsets

from api.models import Review
from api.serializers.review_serializer import ReviewSerializer


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
