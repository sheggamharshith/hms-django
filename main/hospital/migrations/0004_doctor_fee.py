# Generated by Django 4.1.2 on 2022-11-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0003_alter_doctor_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="fee",
            field=models.IntegerField(default=100),
        ),
    ]
