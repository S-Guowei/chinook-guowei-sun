from django.db import models

# Create your models here.
class Track(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=50)
    composer = models.CharField(max_length=100)
    milliseconds = models.IntegerField
    bytes = models.IntegerField
    bytes = models.FloatField
    unitPrice = models.IntegerField
    albums = models.ForeignKey('Album',related_name="track_album")
    
class Album(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=100)
    artists = models.ForeignKey('Artist',related_name="album_artist")
    
class Artist(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=50)
