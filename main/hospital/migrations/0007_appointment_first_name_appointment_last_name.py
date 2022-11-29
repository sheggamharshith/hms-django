# Generated by Django 4.1.2 on 2022-11-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0006_remove_appointment_patient_appointment_age_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="first_name",
            field=models.CharField(default="default_name", max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appointment",
            name="last_name",
            field=models.CharField(default="default_name_2", max_length=254),
            preserve_default=False,
        ),
    ]
