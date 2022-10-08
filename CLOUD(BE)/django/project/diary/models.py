from django.db import models

# Create your models here.

class diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    USER_ID = models.CharField(max_length=36)