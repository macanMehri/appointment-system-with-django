from .models import (
    Patient, Report, PatientsReports, Medicine, Service, Reservation, AvailableTimes, UsersSuggestion,
    Doctor, DoctorsServices
)
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor

        fields = (
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
        model = User

        extra_kwargs = {'password': {'write_only': True}}

        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        patient = Patient.objects.create(user=user)
        patient.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


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
    doctor = DoctorSerializer()
    service = ServiceSerializer()

    class Meta:
        model = DoctorsServices

        fields = ('doctor', 'service')


class ReservationSerializer(serializers.ModelSerializer):
    doctor_and_service = DoctorsServicesSerializer()

    class Meta:
        model = Reservation

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

    patient = PatientSerializer()
    report = ReportSerializer()
    medicine = MedicineSerializer()

    class Meta:
        model = PatientsReports

        fields = (
            'id',
            'medicine_count',
            'medicine_description',
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
