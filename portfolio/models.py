from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    link = models.URLField()
    
class Screenshots(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField()
# Create your models here.
