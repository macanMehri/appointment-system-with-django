from datetime import datetime

from django.contrib.postgres.fields import ranges
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, User


GENDER_CHOICES = (
    ('مرد', 'مرد'),
    ('زن', 'زن'),
)
REPORT_CHOICES = (
    ('پیشنهاد', 'پیشنهاد'),
    ('انتقاد', 'انتقاد')
)


class BaseModel(models.Model):
    """A base class for other models"""
    is_active = models.BooleanField(
        default=False,
        verbose_name='فعال'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد شده'
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ تغییر داده شده'
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        raise NotImplementedError('You did not override the string method!')


class Doctor(BaseModel):
    """A class for doctors working in the clinic"""
    first_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='نام'
    )
    last_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='نام خانوادگی'
    )
    password = models.CharField(
        max_length=20,
        blank=False,
        verbose_name='رمز عبور'
    )
    phone_number = models.CharField(
        max_length=11,
        blank=False,
        verbose_name='شماره تماس'
    )
    national_code = models.CharField(
        max_length=10,
        primary_key=True,
        verbose_name='کد ملی',
    )

    class Meta:
        verbose_name = 'پزشک'
        verbose_name_plural = 'پزشک ها'

    def __str__(self) -> str:
        return f'{self.first_name}-{self.last_name}'


class UsersSuggestion(BaseModel):
    """A class for users suggestions and criticism"""
    title = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='موضوع'
    )
    type = models.CharField(
        max_length=9,
        choices=REPORT_CHOICES,
        default='پیشنهاد',
        verbose_name='نوع'
    )
    description = models.TextField(
        blank=False,
        verbose_name='توضیحات'
    )

    class Meta:
        verbose_name = 'پیشنهاد و انتقاد'
        verbose_name_plural = 'پیشنهادات و انتقادات'

    def __str__(self) -> str:
        return f'{self.title}-{self.type}: {self.description}'


class AvailableTimes(BaseModel):
    """A class to show open times for reservation"""
    available_time = models.DateTimeField(
        verbose_name='تاریخ'
    )

    class Meta:
        verbose_name = 'نوبت آزاد'
        verbose_name_plural = 'نوبت های آزاد'

    def __str__(self) -> str:
        return f'{self.available_time}'


class Service(BaseModel):
    """A class for services"""
    title = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='موضوع'
    )
    cost = models.FloatField(
        validators=[MinValueValidator(1)],
        verbose_name='هزینه'
    )

    class Meta:
        verbose_name = 'سرویس'
        verbose_name_plural = 'سرویس ها'

    def __str__(self) -> str:
        return f'{self.title}: {self.cost}'


class DoctorsServices(BaseModel):
    """A class to dedicate services to doctors"""
    doctor = models.ForeignKey(Doctor, on_delete=models.deletion.CASCADE, verbose_name='پزشک')
    service = models.ForeignKey(Service, on_delete=models.deletion.CASCADE, verbose_name='خدمت')

    class Meta:
        verbose_name = 'خدمت پزشک'
        verbose_name_plural = 'خدمات پزشک'

    def __str__(self):
        return f'{self.doctor} : {self.service}'


class Reservation(BaseModel):
    """A class for reserves"""
    date = models.DateTimeField(
        verbose_name='تاریخ'
    )
    doctor_and_service = models.ForeignKey(
        DoctorsServices,
        on_delete=models.deletion.CASCADE,
        verbose_name='خدمات و پزشک',
    )

    class Meta:
        verbose_name = 'نوبت'
        verbose_name_plural = 'نوبت ها'

    def __str__(self) -> str:
        return f'{self.date}:\n{self.doctor_and_service}'


class Report(BaseModel):
    """An object for patients reports"""
    title = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='تشخیص'
    )
    description = models.TextField(
        blank=False,
        verbose_name='توضیحات'
    )

    class Meta:
        verbose_name = 'گزارش'
        verbose_name_plural = 'گزارشات'

    def __str__(self):
        return f'{self.title}\n{self.description}'


class Patient(BaseModel):
    """A class for patients"""

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='کاربر')

    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='نام',
        default=None,
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='نام خانوادگی',
        default=None,
    )
    phone_number = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name='شماره تماس',
        default=None,
    )
    sex = models.CharField(
        max_length=9,
        choices=GENDER_CHOICES,
        default=None,
        verbose_name='جنسیت',
        null=True,
    )
    birth_day = models.DateField(
        verbose_name='تاریخ تولد',
        blank=True,
        null=True,
        default=None,
    )
    file_number = models.IntegerField(
        verbose_name='شماره پرونده',
        blank=True,
        null=True,
        default=None,
    )

    reservation = models.ForeignKey(
        Reservation,
        null=True,
        on_delete=models.deletion.CASCADE,
        verbose_name='نوبت'
    )

    class Meta:
        verbose_name = 'مراجعه کننده'
        verbose_name_plural = 'مراجعین'

    def __str__(self):
        return (
            f'{self.first_name} ' +
            f'{self.last_name} - ' +
            f'{self.sex} - ' +
            f'{self.birth_day} - ' +
            f'{self.file_number}'
        )


class Medicine(BaseModel):
    """An object of patients medicines"""
    medicine_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='نام دارو',
    )

    class Meta:
        verbose_name = 'دارو'
        verbose_name_plural = 'داروها'

    def __str__(self):
        return f'{self.medicine_name}'


class PatientsReports(BaseModel):
    """A class to dedicate reports to patients"""
    patient = models.ForeignKey(
        Patient,
        on_delete=models.deletion.CASCADE,
        verbose_name='مراجعه کننده',
    )
    report = models.ForeignKey(
        Report,
        on_delete=models.deletion.CASCADE,
        verbose_name='گزارش',
    )
    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.deletion.CASCADE,
        verbose_name='دارو',
    )
    medicine_count = models.IntegerField(verbose_name='تعداد مورد نیاز')
    medicine_description = models.TextField(
        verbose_name='طریقه مصرف',
    )

    class Meta:
        verbose_name = 'گزارش مراجعه کننده'
        verbose_name_plural = 'گزارشات مراجعه کننده'

    def __str__(self):
        return f'{self.patient}: \n{self.report} - {self.medicine} - {self.medicine_count}'
