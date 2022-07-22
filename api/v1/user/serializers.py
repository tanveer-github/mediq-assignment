from django.contrib.auth import get_user_model
from .models import User
from rest_framework import serializers

MIN_LENGTH = 5


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
        }
    )
    password_2 = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "last_name", "gender", "password", "username", "email", "password", "password_2")

    def validate(self, data):
        if data["password"] != data["password_2"]:
            raise serializers.ValidationError("Password does not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            gender=validated_data["gender"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
