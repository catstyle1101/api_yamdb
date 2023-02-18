from django.conf import settings
from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data

        title_id = self.context['view'].kwargs.get('title_id')
        author = self.context['request'].user
        if Review.objects.filter(
                author=author, title=title_id).exists():
            raise serializers.ValidationError(
                'Нельзя писать больше одного отзыва к произведению'
            )
        return data

    def validate_score(self, value):
        if not settings.MIN_RATING <= value <= settings.MAX_RATING:
            raise serializers.ValidationError(
                f'Оценка должна быть в диапазоне от {settings.MIN_RATING} '
                f'до {settings.MAX_RATING}'
            )
        return value
