# Generated by Django 4.1.2 on 2022-11-22 06:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hospital", "0005_patient_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appointment",
            name="patient",
        ),
        migrations.AddField(
            model_name="appointment",
            name="age",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appointment",
            name="dob",
            field=models.DateField(
                default=datetime.datetime(2022, 11, 22, 6, 3, 14, 810785)
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appointment",
            name="guardian_name",
            field=models.CharField(default="asdsadas", max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appointment",
            name="location",
            field=models.CharField(default="asdasdasd", max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appointment",
            name="sex",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default="M",
                max_length=1,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appointment",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]