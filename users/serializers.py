from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from .models import Profile, EditorProfile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    # birthday = serializers.DateField(required=True)
    # address = serializers.CharField(required=True)
    # nickname = serializers.CharField(required=True)
    
    class Meta:
        model = Profile.user.field.related_model
        fields = ('username', 'password', 'password2') #"birthday", "address", "nickname"
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "비밀번호가 일치하지 않습니다!"}
            )
        
        return data
    
    def create(self, validated_data):
        user = Profile.user.field.related_model.objects.create_user(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
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
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'birthday', 'nickname', 'address']
        

class EditorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorProfile
        fields = ['user', 'name', 'address']

    def create(self, validated_data):
        user = self.context['request'].user

        if not user.is_authenticated:
            raise serializers.ValidationError("로그인한 사용자만 프로필을 생성할 수 있습니다.")

        validated_data['user'] = user
        editor_profile = EditorProfile.objects.create(**validated_data)
        return editor_profile