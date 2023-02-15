from rest_framework import serializers

from api.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )

    class Meta:
        model = Review
        fields = ("id", "text", "author", "score", "pub_date")
