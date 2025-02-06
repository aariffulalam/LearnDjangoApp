from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")