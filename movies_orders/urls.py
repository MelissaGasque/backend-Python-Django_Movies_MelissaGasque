from django.urls import path
from .views import MoviesOrderView


urlpatterns = [
    path("movies/<int:movie_id>/orders/", MoviesOrderView.as_view()),
]
