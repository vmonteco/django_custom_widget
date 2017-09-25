from django.core.urlresolvers import reverse
from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=30, unique=True)
    img = models.ImageField(upload_to="img")

    def get_absolute_url(self):
        return reverse("main:picture_detail", kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=30, unique=True)
    imgs = models.ManyToManyField(Picture, related_name="lists", blank=True)

    def get_absolute_url(self):
        return reverse("main:list_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
