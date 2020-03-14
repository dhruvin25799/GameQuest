from django.db import models

# Create your models here.


class Membership(models.Model):
    rank = models.CharField(max_length=50, primary_key=True)
    eligibility = models.PositiveIntegerField()
    discount_offered = models.PositiveIntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.rank
