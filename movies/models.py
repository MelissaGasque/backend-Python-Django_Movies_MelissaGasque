from django.db import models


class RatingChoices(models.TextChoices):
    RATED_G = "G",
    RATED_PG = "PG",
    RATED_PG_13 = "PG-13",
    RATED_R = "R",
    RATED_NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, default="")
    rating = models.CharField(
        max_length=20,
        choices=RatingChoices.choices,
        default=RatingChoices.RATED_G
    )
    synopsis = models.TextField(blank=True, default="")
    user = models.ForeignKey(
        "users.User",
        related_name="movies",
        on_delete=models.CASCADE
    )
