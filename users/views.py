from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import Profile
from users.serializers import ProfileSerializer, UserSerializer
from django.contrib.auth import logout


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "회원 탈퇴 완료!"}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def delete(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"message": "로그아웃 완료!"}, status=status.HTTP_204_NO_CONTENT)


class ProfileView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            profile = Profile.objects.all()
            serializer = ProfileSerializer(profile, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)