from rest_framework import serializers
from users.models import User
from rest_framework.views import status


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=127)
    password = serializers.CharField(max_length=128, write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(default=None)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False, read_only=True)

    def create(self, validated_data):
        # username = validated_data.get('username')
        # email = validated_data.get('email')

        # if User.objects.filter(username=username).exists():
        #     raise serializers.ValidationError(
        #         "username already taken.",
        #         status.HTTP_400_BAD_REQUEST
        #     )

        # if User.objects.filter(email=email).exists():
        #     raise serializers.ValidationError(
        #         "email already registered.",
        #         status.HTTP_400_BAD_REQUEST
        #     )

        if validated_data['is_employee']:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user