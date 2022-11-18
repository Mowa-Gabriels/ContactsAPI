from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed



class UserSerializer(ModelSerializer):

    email = serializers.EmailField(min_length = 4, max_length = 255)
    first_name = serializers.CharField(min_length = 2, max_length = 255)
    last_name = serializers.CharField(min_length = 2, max_length = 255)
    password = serializers.CharField(
        max_length=65, min_length=8, write_only = True
    )


    class Meta:

        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        # extra_kwargs = {
        #     'password': {'required': True}
        # }

    def validate(self, attrs):

        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')}
            )
        return super().validate(attrs)

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
        

    
class LoginSerializer(serializers.ModelSerializer):
 
    password= serializers.CharField(max_length= 225, write_only =True)
    username= serializers.CharField(max_length= 225)
  
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
