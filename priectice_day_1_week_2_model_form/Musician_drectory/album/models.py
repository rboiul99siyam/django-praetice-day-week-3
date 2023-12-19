from django.db import models

from musician.models import Musicians


class Album_form(models.Model):
    album_name = models.CharField(max_length=50)
    album_release_date = models.DateTimeField()
    album_rating = models.IntegerField()
    musician = models.ForeignKey(Musicians, on_delete=models.CASCADE, default=None)


    def __str__(self) -> str:
        return self.album_name
