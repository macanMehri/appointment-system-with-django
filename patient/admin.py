from django.contrib import admin
from .models import (
    Patient, Report, PatientsReports, Medicine, Service, Reservation, Account, AvailableTimes, UsersSuggestion
)


# My actions
@admin.action(description='فعال سازی گزینه های انتخاب شده')
def activate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='غیر فعال کردن گزینه های انتخاب شده')
def deactivate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=False)


class BaseAdmin(admin.ModelAdmin):

    # Actions
    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )


@admin.register(Account)
class AdminAccount(BaseAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
        'password',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'first_name', 'last_name')
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by national code
    ordering = ('pk',)

    search_fields = ('id', 'first_name', 'last_name', 'phone_number')


@admin.register(Service)
class AdminService(BaseAdmin):
    list_display = (
        'id',
        'title',
        'cost',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active', 'cost')
    # Order by national code
    ordering = ('pk',)

    search_fields = ('id', 'title')


@admin.register(AvailableTimes)
class AdminAvailableTimes(BaseAdmin):
    list_display = (
        'id',
        'available_time',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'available_time')
    list_filter = ('available_time', 'is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by national code
    ordering = ('pk',)

    search_fields = ('id', 'available_time')


@admin.register(Reservation)
class AdminReservation(BaseAdmin):
    list_display = (
        'id',
        'date',
        'service',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id',)
    list_filter = ('is_active', 'created_date', 'updated_date', 'date')
    list_editable = ('is_active',)
    # Order by national code
    ordering = ('pk',)

    search_fields = ('id', 'service__title', 'service__cost')


@admin.register(Patient)
class AdminPatient(BaseAdmin):
    list_display = (
        'national_code',
        'first_name',
        'last_name',
        'phone_number',
        'birth_day',
        'سن',
        'sex',
        'file_number',
        'reservation',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('national_code', 'first_name', 'file_number',)
    list_filter = ('is_active', 'reservation__date', 'created_date', 'updated_date', 'sex', 'birth_day')
    list_editable = ('is_active', 'sex')
    # Order by national code
    ordering = ('national_code',)

    search_fields = (
        'national_code',
        'first_name',
        'last_name',
        'file_number',
        'reservation__service__title',
        'phone_number',
    )


@admin.register(Report)
class AdminReport(BaseAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by national code
    ordering = ('pk',)

    search_fields = ('title', 'description')


@admin.register(PatientsReports)
class AdminPatientsReports(BaseAdmin):
    list_display = (
        'id',
        'patient',
        'report',
        'medicine',
        'medicine_count',
        'medicine_description',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'patient', 'report', 'medicine')
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by national code
    ordering = ('pk',)

    search_fields = (
        'patient__national_code',
        'patient__file_number',
        'patient__first_name',
        'patient__last_name',
        'medicine__medicine_name',
        'report__title',
    )


@admin.register(Medicine)
class AdminMedicine(BaseAdmin):
    list_display = (
        'id',
        'medicine_name',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('medicine_name',)
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by national code
    ordering = ('pk',)

    search_fields = ('medicine_name',)


@admin.register(UsersSuggestion)
class AdminUsersSuggestion(BaseAdmin):
    list_display = (
        'id',
        'title',
        'type',
        'description',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('title', 'type', 'is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by national code
    ordering = ('pk',)

    search_fields = ('title', 'type')
