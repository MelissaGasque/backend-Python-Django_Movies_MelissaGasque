from rest_framework import serializers
from .models import Movie, RatingChoices
from users.serializers import UserSerializer


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default="")
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices,
        default=RatingChoices.RATED_G
    )
    synopsis = serializers.CharField(allow_blank=True, default="")
    added_by = serializers.CharField(read_only=True, source='user.email')
    user = UserSerializer(),

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie
