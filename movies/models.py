from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    released = models.DateField()
    runtime = models.IntegerField()  # Duration in minutes
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    actors = models.TextField()
    plot = models.TextField()
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    awards = models.TextField()
    poster = models.URLField()
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)  # IMDb rating

    def __str__(self):
        return self.title
