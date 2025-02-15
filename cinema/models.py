from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f"Actor: {self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=64)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return (
            f"Cinema Hall: {self.name}, rows: {self.rows}, "
            f"seats in row: {self.seats_in_row}"
        )


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
