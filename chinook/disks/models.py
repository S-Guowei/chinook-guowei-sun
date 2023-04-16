from django.db import models

# Create your models here.
class Track(models.Model):
    
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200,null=True)
    milliseconds = models.IntegerField('Duration (ms)')
    bytes = models.IntegerField('Size (bytes)')
    unitPrice = models.FloatField('Unit Price (EUR)')
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Album(models.Model):

    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
class Artist(models.Model):
  
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name