from django.db import models

# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    breed = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name
