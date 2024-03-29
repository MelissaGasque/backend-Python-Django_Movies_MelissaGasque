from rest_framework.views import APIView, status, Request, Response
from movies.models import Movie
from .serializers import MovieOrdersSerialaizer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class MoviesOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:  
        found_movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrdersSerialaizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, movie=found_movie)
        return Response(serializer.data, status.HTTP_201_CREATED)
