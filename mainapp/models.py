from django.db import models
from datetime import datetime
# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    image_path = models.CharField(max_length=600)
    description = models.TextField()
    author = models.CharField(max_length=100)
    end_time = models.DateTimeField()
    create_date = models.DateTimeField(default=datetime.now)
