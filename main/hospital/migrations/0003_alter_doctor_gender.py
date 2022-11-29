# Generated by Django 4.1.2 on 2022-11-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0002_doctor_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], max_length=1
            ),
        ),
    ]
