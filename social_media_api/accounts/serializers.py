from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Explicitly using serializers.CharField()
    token = serializers.SerializerMethodField()  # Adding token field to response

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password', 'token']

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)  # Explicitly calling Token.objects.create
        return token.key

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)  # Explicitly creating a token on user registration
        return user
