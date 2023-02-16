from rest_framework import serializers
from api.models.titles import Titles
from api.models.genres import Genre
from api.models.categories import Categories
from api.serializers.genres_serializer import GenreSerializer
from api.serializers.categories_serizlizer import CategorySerializer


class GetTitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        fields = (
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category'
        )
        model = Titles


class TitlesSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        required=False,
        queryset=Genre.objects.all(),
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        many=False,
        required=False,
        queryset=Categories.objects.all(),
    )

    class Meta:
        fields = (
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category'
        )
        model = Titles
