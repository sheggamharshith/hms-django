from django.urls import path, re_path
from .views import (
    HomePageView,
    DoctorAdminView,
    DoctorAdminAddView,
    DoctorAdminDeleteView,
    PatientView,
    DepartmentView,
    DepartmentAddView,
    DepartmentUserView,
    DepartmentAddUserView,
    AppointmentCreateView,
    AppointmentListView,
    AppointmentDeleteView,
    AppointmentDepartmentView,
    AppointmentApprovalDepartmentView,
    DoctorPatientView,
    PrescriptionAddView,
    PrescriptionView,
)

urlpatterns = [
    path("home", HomePageView.as_view(), name="home"),
    path("admin_doctor", DoctorAdminView.as_view(), name="admin_doctor"),
    path("admin_doctor_add", DoctorAdminAddView.as_view(), name="admin_doctor_add"),
    path(
        "admin_doctor_delete/<int:id>",
        DoctorAdminDeleteView.as_view(),
        name="admin_doctor_delete",
    ),
    path(
        "admin_patient/",
        PatientView.as_view(),
        name="admin_patient",
    ),
    path(
        "admin_patient/<int:id>",
        PatientView.as_view(),
        name="admin_patient_status",
    ),
    path(
        "admin_department/",
        DepartmentView.as_view(),
        name="admin_department",
    ),
    path(
        "admin_department/<int:id>",
        DepartmentView.as_view(),
        name="admin_department",
    ),
    path(
        "admin_department_add",
        DepartmentAddView.as_view(),
        name="admin_department_add",
    ),
    path(
        "admin_department_user/<uuid:id>",
        DepartmentUserView.as_view(),
        name="admin_department_user",
    ),
    path(
        "admin_department_user",
        DepartmentUserView.as_view(),
        name="admin_department_user",
    ),
    path(
        "admin_department_add_user",
        DepartmentAddUserView.as_view(),
        name="admin_department_add_user",
    ),
    path(
        "appointment",
        AppointmentCreateView.as_view(),
        name="create_appointment",
    ),
    path("view_appointment", AppointmentListView.as_view(), name="view_appointment"),
    path(
        "delete_appointment/<pk>",
        AppointmentDeleteView.as_view(),
        name="delete_appointment",
    ),
    path(
        "department-appointment",
        AppointmentDepartmentView.as_view(),
        name="department_appointment_view",
    ),
    path(
        "department-approval/<id>",
        AppointmentApprovalDepartmentView.as_view(),
        name="department_appointment_approval",
    ),
    path(
        "doctor-patient",
        DoctorPatientView.as_view(),
        name="doctor_patient",
    ),
    path(
        "prescription-add/<id>",
        PrescriptionAddView.as_view(),
        name="doctor_prs",
    ),
    path(
        "prescription-view/<id>",
        PrescriptionView.as_view(),
        name="doctor_prs_view",
    ),
]
