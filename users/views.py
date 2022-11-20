from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer
from django.contrib.auth import logout


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # # 회원탈퇴
    # def delete(self, request, **kwargs):
    #     if kwargs.get('user_id') is None:
    #         return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         user_id = kwargs.get('user_id')
    #         user_object = User.objects.get(id=user_id)
    #         user_object.delete()
    #         return Response("delete ok", status=status.HTTP_200_OK)


class LogoutView(APIView):
    def delete(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'message': 'logout complete'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'invalid request'}, status=status.HTTP_200_OK)