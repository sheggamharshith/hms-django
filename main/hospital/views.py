from django.shortcuts import HttpResponseRedirect, render, redirect
from django.views.generic.base import View
from django.views.generic import DeleteView
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.permission import SuperUserRequiredMixin
from .forms import DoctorForm, DepartmentForm, AppointmentForm, AppointmentBookRoomForm
from .models import Doctor, Department, Appointment, Patient
from user.models import User
from user.forms import DepartmentUserForm

# Create your views here.
class HomePageView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser:
            context = {}
            doctors = Doctor.objects.all()
            patients = Patient.objects.all()
            context["doctors"] = doctors
            context["patients"] = patients
            context["doctor_count"] = doctors.count()
            context["department_count"] = Department.objects.all().count()
            context["appointment_count"] = Appointment.objects.all().count()
            context["patient_count"] = patients.count()
            return render(request, "home.html", context)
        if request.user.user_type == "PT":
            return render(request, "patient_home.html")
        if request.user.user_type == "DP":
            return render(request, "department_home.html")


class DoctorAdminView(SuperUserRequiredMixin, View):
    def get(self, request):
        context = {}
        context["doctors"] = Doctor.objects.all()
        return render(request, "doctor_admin.html", context)


class DoctorAdminAddView(SuperUserRequiredMixin, View):
    def get(self, request):
        form = DoctorForm()
        return render(request, "doctor_add.html", {"form": form})

    def post(self, request):
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect("/admin_doctor")
        return render(request, "doctor_add.html", {"form": form})


class DoctorAdminDeleteView(SuperUserRequiredMixin, View):
    def get(self, request, id):
        try:
            Doctor.objects.get(id=id).delete()
        except Exception as e:
            print(e)
        return redirect("/admin_doctor")

    def post(self, request, id):
        try:
            doctor = Doctor.objects.get(id=id)
            doctor.is_active = not doctor.is_active
            doctor.user.is_active = not doctor.user.is_active
            doctor.save()
            return redirect("/admin_doctor")
        except Exception as e:
            print(e)


class PatientView(SuperUserRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        context["patients"] = Patient.objects.all()
        return render(request, "admin_patient.html", context)

    def post(self, request, id):
        try:
            patient = Patient.objects.get(id=id)
            patient.user.is_active = not patient.user.is_active
            patient.user.save()
            patient.save()
            return redirect("/admin_patient/")
        except Exception as e:
            print(e)
            pass


class DepartmentView(SuperUserRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        context["departments"] = Department.objects.all()
        context["users"] = User.objects.filter(user_type="DP")
        return render(request, "admin_department.html", context)

    def post(self, request, id):
        try:
            Department.objects.get(id=id).delete()
            return redirect("/admin_department/")
        except Exception as e:
            print(e)
            pass


class DepartmentAddView(SuperUserRequiredMixin, View):
    def get(self, request):
        return render(request, "admin_department_add.html", {"form": DepartmentForm()})

    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect("/admin_department/")
        return render(request, "admin_department_add.html", {"form": form})


class DepartmentUserView(SuperUserRequiredMixin, View):
    def get(self, request, id):
        try:
            User.objects.get(id=id).delete()
            return redirect("/admin_department/")
        except Exception as e:
            print(e)
            pass

    def post(self, request, id):
        try:
            User.objects.get(id=id).delete()
            return redirect("/admin_department/")
        except Exception as e:
            print(e)


class DepartmentAddUserView(SuperUserRequiredMixin, View):
    def get(self, request):
        return render(
            request, "admin_department_user.html", {"form": DepartmentUserForm()}
        )

    def post(self, request):
        print("here")
        form = DepartmentUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/admin_department/")
        return render(request, "admin_department_user.html", {"form": form})


class AppointmentCreateView(LoginRequiredMixin, FormView, CreateView):
    template_name: str = "appointment_Create.html"
    form_class = AppointmentForm
    success_url = "/appointment"

    def get_initial(self):
        return {"user": self.request.user, "status": "P"}


class AppointmentListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        context["appointments"] = Appointment.objects.filter(
            user__email=request.user.email
        )
        return render(request, "patient_app_view.html", context)


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "appiontment_delete.html"
    model = Appointment
    success_url = "/view_appointment"


class AppointmentDepartmentView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        context["appointments"] = Appointment.objects.filter(status="P")
        return render(request, "department_appointment_view.html", context)


class AppointmentApprovalDepartmentView(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        context["form"] = AppointmentBookRoomForm(
            initial={"Appointment": Appointment.objects.get(id=id)}
        )
        return render(request, "department_approval_view.html", context)

    def post(self, request, id=None):
        form = AppointmentBookRoomForm(data=request.POST)
        if form.is_valid():
            form.save()
            ap = Appointment.objects.get(id=id)
            ap.status = "A"
            ap.save()
            return redirect("/department-appointment")
        return render(request, "department_approval_view.html", {"form": form})
