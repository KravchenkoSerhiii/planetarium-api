from django.db import models
from django.conf import settings


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=65)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class AstronomyShow(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField()

    def __str__(self):
        return self.title


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(AstronomyShow, on_delete=models.CASCADE, related_name="show_sessions")
    planetarium_dome = models.ForeignKey(PlanetariumDome, on_delete=models.CASCADE, related_name="show_sessions")
    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.astronomy_show}. Place: {self.planetarium_dome}"


class ShowTheme(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ["-created_at"]


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey(ShowSession, on_delete=models.CASCADE, related_name="tickets")
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="tickets")

    def __str__(self):
        return f"{self.show_session}: {self.row}, {self.seat}"

    class Meta:
        unique_together = ("show_session", "row", "seat")
        ordering = ["row", "seat"]
