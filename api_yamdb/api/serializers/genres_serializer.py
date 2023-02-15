from rest_framework import serializers
from api.models.genres import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['id',]
