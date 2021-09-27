from django.db import models

class WallPaper(models.Model):
    text = models.CharField(max_length=100)
    image = models.ImageField('image')
