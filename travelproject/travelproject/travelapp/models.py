from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()


class team(models.Model):
    names = models.CharField(max_length=250)
    imag = models.ImageField(upload_to='pics')
    desgntn = models.TextField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.names
