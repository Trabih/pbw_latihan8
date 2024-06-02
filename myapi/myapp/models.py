from django.db import models

# Create your models here.
class Journal (models.Model):
    author = models.CharField(max_length = 50)
    title = models.CharField(max_length= 100)
    year = models.IntegerField()

    def __str__(self):
        return self.title