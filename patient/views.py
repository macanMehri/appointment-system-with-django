from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import (
    PatientSerializer, ReportSerializer, PatientsReportsSerializer, MedicineSerializer, ServiceSerializer,
    ReservationSerializer, AccountSerializer, AvailableTimesSerializer, UsersSuggestionSerializer,
    DoctorSerializer, DoctorsServicesSerializer, CustomTokenObtainPairSerializer, ProfileSerializer
)
from django.contrib.auth.models import User
from .models import (
    Patient, Report, PatientsReports, Medicine, Service, Reservation, AvailableTimes, UsersSuggestion,
    Doctor, DoctorsServices,
)


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountSerializer


class SignInView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class DoctorViewSet(viewsets.ModelViewSet):
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
