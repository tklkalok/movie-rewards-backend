from django.db import models

# Create your models here.
class Movie(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=4)
    Rated = models.CharField(max_length=10, blank=True)
    Released = models.CharField(max_length=20, blank=True)
    Runtime = models.CharField(max_length=10, blank=True)
    Genre = models.CharField(max_length=100, blank=True)
    Director = models.CharField(max_length=100, blank=True)
    Writer = models.CharField(max_length=200, blank=True)
    Actors = models.CharField(max_length=500, blank=True)
    Plot = models.TextField(blank=True)
    Language = models.CharField(max_length=50, blank=True)
    Country = models.CharField(max_length=50, blank=True)
    Awards = models.TextField(blank=True)
    Poster = models.URLField(blank=True)
    Ratings = models.TextField(blank=True)
    Metascore = models.CharField(max_length=10, blank=True)
    imdbRating = models.CharField(max_length=4, blank=True)
    imdbVotes = models.CharField(max_length=10, blank=True)
    imdbID = models.CharField(max_length=20, blank=True)
    Type = models.CharField(max_length=20, blank=True)
    DVD = models.CharField(max_length=20, blank=True)
    BoxOffice = models.CharField(max_length=20, blank=True)
    Production = models.CharField(max_length=50, blank=True)
    Website = models.URLField(blank=True)
    Response = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.Title