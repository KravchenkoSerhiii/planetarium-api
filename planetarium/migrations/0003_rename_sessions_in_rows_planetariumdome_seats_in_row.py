# Generated by Django 5.0.6 on 2024-06-10 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("planetarium", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="planetariumdome",
            old_name="sessions_in_rows",
            new_name="seats_in_row",
        ),
    ]
