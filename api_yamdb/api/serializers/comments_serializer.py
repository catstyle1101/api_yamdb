from rest_framework import serializers

from api.models import Comments


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )

    class Meta:
        model = Comments
        fields = ("id", "text", "author", "pub_date")
