from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "pk",
            "email",
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )
    extra_kwargs = {
        "password": {"write_only": "True"},
    }

    class Meta:
        model = User
        fields = ["email", "password", "password2"]

    def save(self):
        user = User(
            email=self.validated_data["email"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"password": "passwords must match"})
        user.set_password(password)
        user.save()
        return user
