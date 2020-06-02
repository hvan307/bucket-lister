from django.db import models
# from django.contrib.auth.models import AbstractUser


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name} {self.description}'

class PlaceToVisit(models.Model):
    name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def _str_(self):
        return f'{self.name} {self.city} {self.country}'

class User(models.Model):
    activities = models.ForeignKey(Activity, related_name='users', on_delete=models.CASCADE, blank=True)
    places_to_visit = models.ForeignKey(PlaceToVisit, related_name='users', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.username
