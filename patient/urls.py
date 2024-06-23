from django.urls import path, include
from .views import (
    PatientViewSet, ReportViewSet, PatientsReportsViewSet, MedicineViewSet, ServiceViewSet, ReservationViewSet,
    AccountViewSet, AvailableTimesViewSet, UsersSuggestionViewSet, DoctorViewSet, DoctorsServicesViewSet, SignUpView,
    SignInView
)
from rest_framework import routers

doctor_router = routers.DefaultRouter()
doctor_router.register('', DoctorViewSet)

patient_router = routers.DefaultRouter()
patient_router.register('', PatientViewSet)

report_router = routers.DefaultRouter()
report_router.register('', ReportViewSet)

patients_report_router = routers.DefaultRouter()
patients_report_router.register('', PatientsReportsViewSet)

medicine_report_router = routers.DefaultRouter()
medicine_report_router.register('', MedicineViewSet)

service_report_router = routers.DefaultRouter()
service_report_router.register('', ServiceViewSet)

reservation_report_router = routers.DefaultRouter()
reservation_report_router.register('', ReservationViewSet)

account_router = routers.DefaultRouter()
account_router.register('', AccountViewSet)

available_time_report_router = routers.DefaultRouter()
available_time_report_router.register('', AvailableTimesViewSet)

user_suggestion_report_router = routers.DefaultRouter()
user_suggestion_report_router.register('', UsersSuggestionViewSet)

doctor_services_report_router = routers.DefaultRouter()
doctor_services_report_router.register('', DoctorsServicesViewSet)

urlpatterns = [
    path('doctor_api/', include(doctor_router.urls,)),
    path('patient_api/', include(patient_router.urls,)),
    path('report_api/', include(report_router.urls,)),
    path('patients_report_api/', include(patients_report_router.urls,)),
    path('medicine_report_api/', include(medicine_report_router.urls,)),
    path('service_report_api/', include(service_report_router.urls,)),
    path('reservation_report_api/', include(reservation_report_router.urls,)),
    path('account_api/', include(account_router.urls,)),
    path('available_time_report_api/', include(available_time_report_router.urls,)),
    path('user_suggestion_report_api/', include(user_suggestion_report_router.urls,)),
    path('doctor_services_report_api/', include(doctor_services_report_router.urls,)),
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/signin/', SignInView.as_view(), name='signin'),
]
