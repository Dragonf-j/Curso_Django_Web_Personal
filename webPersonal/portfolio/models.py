from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    image = models.ImageField()
    created= models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)