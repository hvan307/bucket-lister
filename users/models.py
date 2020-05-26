from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField

    def __str__(self):
        return f'{self.name} {self.description}'

class PlaceToVisit(models.Model):
    name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def _str_(self):
        return f'{self.name} {self.city} {self.country}'

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pass_confirm = models.CharField(max_length=50)
    image = models.CharField(max_length=200, blank=True)
    activities = models.ForeignKey(Activity, related_name='users', on_delete=models.CASCADE, blank=True)
    places_to_visit = models.ForeignKey(PlaceToVisit, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username} {self.email} {self.image} {self.activities} {self.places_to_visit}'
