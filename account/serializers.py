from rest_framework import serializers
from .models import MyUser, WebLinks


class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password', 'password2',)
        extra_Kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        password = data.get('password')
        password2 = data.pop('password2')

        if password != password2:
            raise serializers.ValidationError(
                "password and confirm password does not match")
        return data

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)

    class Meta:
        model = MyUser
        fields = ['email', 'password']


class WebLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebLinks
        fields = ['url']
