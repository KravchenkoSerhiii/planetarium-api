from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

from planetarium.models import (
    PlanetariumDome,
    ShowTheme,
    ShowSession,
    AstronomyShow,
    Reservation,
    Ticket
)
from planetarium.serializers import (
    PlanetariumDomeSerializer,
    ShowThemeSerializer,
    ShowSessionSerializer,
    TicketSerializer,
    AstronomyShowSerializer,
    ReservationSerializer
)


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
