from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',
            'is_superuser', 'last_login', 'date_joined')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

