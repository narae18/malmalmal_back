from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, EditorProfileSerializer
from .models import Profile, EditorProfile


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token":token.key}, status=status.HTTP_200_OK)

class ProfileView(generics.GenericAPIView):
    queryset  = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    
    #프로필 유저 정보 가져오기
    def get(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
class EditorProfileView(generics.GenericAPIView):
    queryset  = EditorProfile.objects.all()
    serializer_class = EditorProfileSerializer