from django.db import models


# Create your models here.
class Swapnil(models.Model):
    coursename = models.CharField(max_length=200)
    facultyname = models.CharField(max_length=200)
