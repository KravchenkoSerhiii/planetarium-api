# Generated by Django 5.0.6 on 2024-06-10 14:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("planetarium", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="showsession",
            name="astronomy_show",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="show_sessions",
                to="planetarium.astronomyshow",
            ),
        ),
        migrations.AddField(
            model_name="showsession",
            name="planetarium_dome",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="show_sessions",
                to="planetarium.planetariumdome",
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="reservation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to="planetarium.reservation",
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="show_session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to="planetarium.showsession",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("show_session", "row", "seat")},
        ),
    ]
