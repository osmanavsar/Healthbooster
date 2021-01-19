from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name + "@" + self.email

class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    population = models.CharField(max_length=50)
    Hospital = models.CharField(max_length=50)
    Bed = models.CharField(max_length=50)
    Ambulance = models.CharField(max_length=50)

