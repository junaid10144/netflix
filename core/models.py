from django.db import models
import uuid

class Movie(models.Model):
    
    # The `GENRE_CHOICES` variable is a tuple of tuples that defines the choices for the `genre` field
    # in the `Movie` model. Each tuple within `GENRE_CHOICES` represents a choice option and consists
    # of two elements: the first element is the value that will be stored in the database, and the
    # second element is the human-readable label that will be displayed in the user interface.
    GENRE_CHOICES = (
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
    )
    
    uu_id = models.UUIDField(default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='movies_images/')
    image_cover = models.ImageField(upload_to='movies_images/')
    video = models.FileField(upload_to='movies_videos/')
    movie_views = models.PositiveIntegerField(default=0)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    
    def __str__(self):
        return self.title
