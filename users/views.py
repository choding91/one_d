from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User, Profile
from users.serializers import FollowingSerializer, ProfileSerializer, UserSerializer
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


class FollowingView(APIView):
    def get(self, request):
        user = request.user
        following = user.following.all()
        serializer = FollowingSerializer(following, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowingUserView(APIView):
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user in user.following.all():
            user.following.remove(request.user)
            return Response("팔로우 취소!", status=status.HTTP_200_OK)
        else:
            user.following.add(request.user)
            return Response("팔로우!", status=status.HTTP_200_OK)
