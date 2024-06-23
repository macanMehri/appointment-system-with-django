from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .serializer import (
    PatientSerializer, ReportSerializer, PatientsReportsSerializer, MedicineSerializer, ServiceSerializer,
    ReservationSerializer, AccountSerializer, AvailableTimesSerializer, UsersSuggestionSerializer,
    DoctorSerializer, DoctorsServicesSerializer,
)
from .models import (
    Patient, Report, PatientsReports, Medicine, Service, Reservation, Account, AvailableTimes, UsersSuggestion,
    Doctor, DoctorsServices,
)


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class PatientViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class PatientsReportsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PatientsReportsSerializer
    queryset = PatientsReports.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class MedicineViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class ReservationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class AvailableTimesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AvailableTimesSerializer
    queryset = AvailableTimes.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class UsersSuggestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UsersSuggestionSerializer
    queryset = UsersSuggestion.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class DoctorsServicesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DoctorsServicesSerializer
    queryset = DoctorsServices.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
