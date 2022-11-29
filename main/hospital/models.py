from django.db import models
from user.models import User

# Create your models here.
class Doctor(models.Model):
    qualification = models.CharField(max_length=254)
    specialization = models.CharField(max_length=254)
    gender = models.CharField(
        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], max_length=1
    )
    experience = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    fee = models.IntegerField(default=100)

    def __str__(self):
        return self.user.first_name


class Patient(models.Model):
    age = models.IntegerField()
    sex = models.CharField(
        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], max_length=1
    )
    guardian_name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    dob = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Department(models.Model):
    name = models.CharField(max_length=254)
    head = models.ForeignKey(User, on_delete=models.CASCADE)


class DoctorDepartment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Appointment(models.Model):
    age = models.IntegerField()
    sex = models.CharField(
        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], max_length=1
    )
    guardian_name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    dob = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(
        choices=[("P", "Pending"), ("A", "Approved")], max_length=1
    )
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    symptoms = models.TextField()
    blood_group = models.CharField(max_length=10)
    note = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)


class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    notes = models.TextField()


class Medicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()


class Room(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)


class AppointmentRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
