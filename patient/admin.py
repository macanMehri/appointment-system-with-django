from django.contrib import admin
from .models import Patient, Report, PatientsReports


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


@admin.register(Patient)
class AdminPatient(BaseAdmin):
    list_display = (
        'national_code',
        'first_name',
        'last_name',
        'birth_day',
        'sex',
        'file_number',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('national_code', 'first_name', 'file_number',)
    list_filter = ('is_active', 'created_date', 'updated_date', 'sex', 'birth_day')
    list_editable = ('is_active', 'sex')
    # Order by national code
    ordering = ('national_code',)

    search_fields = ('national_code', 'first_name', 'last_name', 'file_number')


@admin.register(Report)
class AdminReport(BaseAdmin):
    list_display = (
        'title',
        'description',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('title',)
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by national code
    ordering = ('pk',)

    search_fields = ('title', 'description')


@admin.register(PatientsReports)
class AdminPatientsReports(BaseAdmin):
    list_display = (
        'patient',
        'report',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('patient', 'report')
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    # Order by national code
    ordering = ('pk',)

    search_fields = ('patient__national_code', 'patient__first_name', 'patient__last_name')

