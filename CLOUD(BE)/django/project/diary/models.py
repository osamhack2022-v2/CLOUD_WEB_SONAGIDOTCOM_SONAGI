from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title