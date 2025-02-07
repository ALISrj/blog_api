from rest_framework.response import Response
from users.models import User
from rest_framework import status
from users.api.serializers import UserSerializer, UserRegisterSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView

class RegisterView(APIView):

    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self,request):

        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
