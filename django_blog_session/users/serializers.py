from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "password", "username", "email", "description", "lined_in_url", "contact_number", "status"]

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name= validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            password=validated_data.pop('password'),
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            description=validated_data.pop('description'),
            lined_in_url=validated_data.pop('lined_in_url'),
            contact_number=validated_data.pop('contact_number'),
            status=validated_data.pop('status'),


        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        self.user = authenticate(username=attrs.pop("email"), password=attrs.pop("password"))

        if self.user:
            return attrs
        else:
            raise serializers.ValidationError()
