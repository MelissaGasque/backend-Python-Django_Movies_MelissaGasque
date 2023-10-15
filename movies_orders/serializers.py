from rest_framework import serializers
from .models import MovieOrder


class MovieOrdersSerialaizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True, source='movie.title')
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    purchased_at = serializers.DateTimeField(read_only=True)
    purchased_by = serializers.DateTimeField(
        read_only=True,
        source='user.email'
    )

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)