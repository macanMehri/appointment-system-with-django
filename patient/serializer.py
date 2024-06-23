from .models import (
    Patient, Report, PatientsReports, Medicine, Service, Reservation, Account, AvailableTimes, UsersSuggestion,
    Doctor, DoctorsServices,
)
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor

        fields = (
            'national_code',
            'first_name',
            'last_name',
            'password',
            'phone_number'
        )


class UsersSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersSuggestion

        fields = (
            'id',
            'title',
            'type',
            'description'
        )


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'password'
        )


class AvailableTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTimes

        fields = (
            'id',
            'available_time',
        )


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service

        fields = (
            'id',
            'title',
            'cost',
        )


class DoctorsServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsServices

        doctor = DoctorSerializer
        service = ServiceSerializer


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation

        doctor_and_service = DoctorsServicesSerializer

        fields = (
            'id',
            'date',
        )


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report

        fields = (
            'id',
            'title',
            'description',
        )


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient

        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'sex',
            'birth_day',
            'national_code',
            'file_number',
        )


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine

        fields = (
            'id',
            'medicine_name',
        )


class PatientsReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientsReports

        patient = PatientSerializer
        report = ReportSerializer
        medicine = MedicineSerializer

        fields = (
            'id',
            'medicine_count',
            'medicine_description',
        )


# class UsersSuggestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UsersSuggestion
#
#         address = AddressSerializer
#
#         fields = (
#             'id',
#             'first_name',
#             'last_name',
#             'number'
#         )

