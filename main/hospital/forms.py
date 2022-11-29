from django import forms
from .models import Doctor, Department, Appointment, AppointmentRoom, Room
from user.models import User
from django.core.exceptions import ValidationError


class DoctorForm(forms.ModelForm):
    email = forms.EmailField(max_length=250)
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    password = forms.CharField(show_hidden_initial=True)

    class Meta:
        model = Doctor
        fields = "__all__"
        exclude = ("is_active", "user")

    def clean(self):
        print(self.data["email"])
        pass

    def save(self, commit: bool = True):
        try:
            user = User.objects.create_doctor(
                email=self.data["email"],
                password=self.data["password"],
                first_name=self.data["first_name"],
                last_name=self.data["last_name"],
            )

            self.cleaned_data["user_id"] = user.id
            del self.cleaned_data["email"]
            del self.cleaned_data["first_name"]
            del self.cleaned_data["last_name"]
            del self.cleaned_data["password"]

            doctor = Doctor(**self.cleaned_data)
            doctor.save()
            return doctor

        except Exception as e:
            if user:
                user.delete()
            raise ValidationError("user already exists")


class DepartmentForm(forms.ModelForm):
    head = forms.ModelChoiceField(queryset=User.objects.filter(user_type="DP"))

    class Meta:
        model = Department
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    date = forms.DateTimeField(widget=forms.TextInput(attrs={"type": "datetime-local"}))

    class Meta:
        model = Appointment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].disabled = True
        self.fields["status"].disabled = True


class AppointmentBookRoomForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Room.objects.filter(is_booked=False))

    class Meta:
        model = AppointmentRoom
        fields = "__all__"
