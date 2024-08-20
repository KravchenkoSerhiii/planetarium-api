from django.contrib import admin

from planetarium.models import (
    PlanetariumDome,
    Reservation,
    Ticket,
    ShowTheme,
    ShowSession,
    AstronomyShow
)

admin.site.register(PlanetariumDome)
admin.site.register(Reservation)
admin.site.register(Ticket)
admin.site.register(ShowTheme)
admin.site.register(ShowSession)
admin.site.register(AstronomyShow)
