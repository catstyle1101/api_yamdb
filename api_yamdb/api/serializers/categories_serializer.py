from rest_framework import serializers

from reviews.models.categories import Categories


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = ('id', )
