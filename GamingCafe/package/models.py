from django.db import models

# Create your models here.


class Package(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    time_added = models.PositiveIntegerField()
    description = models.CharField(max_length=256)
    def __str__(self):
        return self.name
