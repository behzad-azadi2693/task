from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    cell = models.CharField(max_length=11)
    road = models.CharField(max_length=50)
    house_number = models.CharField(max_length=150)


    def __str__(self):
        return f'{self.name}-{self.id}'