from rest_framework.views import Response, APIView, Request, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from .serializers import MovieSerializer
from .models import Movie


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def post(self, req: Request):
        serializer = MovieSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save(user=req.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, req: Request) -> Response:
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, req: Request, movie_id: int) -> Response:
        try:
            found_movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            {"detail": "Not found."}, status.HTTP_404_NOT_FOUND
        serializer = MovieSerializer(found_movie)
        return Response(serializer.data,  status.HTTP_200_OK)

    def delete(self, req: Request, movie_id: int) -> Response:
        try:
            found_movie = Movie.objects.get(id=movie_id)
            found_movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(
                {"detail": "Not found."}, status.HTTP_404_NOT_FOUND
            )
