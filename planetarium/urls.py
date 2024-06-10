from django.urls import path, include
from rest_framework import routers

from planetarium.views import (
    PlanetariumDomeViewSet,
    ShowSessionViewSet,
    ShowThemeViewSet,
    AstronomyShowViewSet,
    TicketViewSet,
    ReservationViewSet,
)

app_name = "planetarium"

router = routers.DefaultRouter()
router.register("planetariums", PlanetariumDomeViewSet)
router.register("show-sessions", ShowSessionViewSet)
router.register("show-themes", ShowThemeViewSet)
router.register("astronomy-shows", AstronomyShowViewSet)
router.register("tickets", TicketViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [
    path("", include(router.urls), name="planetarium")
]
