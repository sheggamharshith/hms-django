# Generated by Django 4.1.2 on 2022-11-20 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[("P", "Pending"), ("A", "Approved")], max_length=1
                    ),
                ),
                ("symptoms", models.TextField()),
                ("blood_group", models.CharField(max_length=10)),
                ("note", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=254)),
                (
                    "head",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qualification", models.CharField(max_length=254)),
                ("specialization", models.CharField(max_length=254)),
                ("gender", models.CharField(max_length=254)),
                ("experience", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.IntegerField()),
                (
                    "sex",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("guardian_name", models.CharField(max_length=254)),
                ("location", models.CharField(max_length=254)),
                ("dob", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Prescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("notes", models.TextField()),
                (
                    "appointment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.appointment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Medicine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                (
                    "prescription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.prescription",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DoctorDepartment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.department",
                    ),
                ),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.doctor",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="appointment",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="hospital.doctor"
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="hospital.patient"
            ),
        ),
    ]
