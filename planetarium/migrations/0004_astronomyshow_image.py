# Generated by Django 5.0.6 on 2024-06-12 13:22

import planetarium.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planetarium", "0003_rename_sessions_in_rows_planetariumdome_seats_in_row"),
    ]

    operations = [
        migrations.AddField(
            model_name="astronomyshow",
            name="image",
            field=models.ImageField(
                null=True, upload_to=planetarium.models.show_image_file_path
            ),
        ),
    ]
