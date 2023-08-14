from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from users.models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')
        read_only_fields = ('editor_name')




class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    profile = ProfileSerializer()
    # birthday = serializers.DateField(required=True)
    # address = serializers.CharField(required=True)
    # nickname = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'profile') #"birthday", "address", "nickname"
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "비밀번호가 일치하지 않습니다!"}
            )
        
        return data
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')  # Extract profile data
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user, **profile_data)  # Create and link profile
        token, created = Token.objects.get_or_create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "로그인 실패ㅠㅠ 아이디 또는 비밀번호가 틀립니다."}
        )
        
        