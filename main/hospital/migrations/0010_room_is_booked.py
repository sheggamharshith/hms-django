# Generated by Django 4.1.2 on 2022-11-28 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0009_room_appointmentroom"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="is_booked",
            field=models.BooleanField(default=False),
        ),
    ]
