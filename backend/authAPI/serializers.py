from django.contrib.auth.models import User  # Import the User model from Django's authentication system
from rest_framework import serializers  # Import serializers from Django REST Fram
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):  # Define a serializer for the User model
    class Meta:  # Meta class to specify metadata options
        model = User  # Specify the User model for the serializer
        fields = ["id", "username" ,"email",  "password"]  # Specify the fields to include in the serialized representation
        extra_kwargs = {"password": {"write_only": True}}  # Specify additional options for the password 
    def validate_password(self, value):
        # Validate password using Django's built-in password validators
        validate_password(value)
        return value

    def create(self, validated_data):  # Method to create a new user
        # Create a new user instance using the validated data
        user = User.objects.create_user(**validated_data)
        return user  # Return the newly created user instance


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
      

