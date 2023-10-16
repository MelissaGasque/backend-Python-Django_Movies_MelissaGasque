from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status, Request, Response
from users.serializers import UserSerializer 
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrAuthenticated


class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAuthenticated]

    def get(self, req: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(found_user)
        return Response(serializer.data)

    def patch(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(
            found_user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
