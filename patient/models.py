from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


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


class Account(BaseModel):
    """A class to store accounts"""
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
    phone_number = models.CharField(
        max_length=11,
        blank=False,
        verbose_name='شماره تماس'
    )
    password = models.CharField(
        max_length=20,
        blank=False,
        verbose_name='رمز عبور'
    )
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'

    def __str__(self) -> str:
        return f'{self.full_name}: {self.phone_number}'


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


class Reservation(BaseModel):
    """A class for reserves"""
    date = models.DateTimeField(
        verbose_name='تاریخ'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.deletion.CASCADE,
        verbose_name='سرویس',
    )

    class Meta:
        verbose_name = 'نوبت'
        verbose_name_plural = 'نوبت ها'

    def __str__(self) -> str:
        return f'{self.date}:\n{self.service}'


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
    phone_number = models.CharField(
        max_length=11,
        blank=False,
        verbose_name='شماره تماس'
    )
    sex = models.CharField(
        max_length=9,
        choices=GENDER_CHOICES,
        default='مرد',
        verbose_name='جنسیت'
    )
    birth_day = models.DateField(
        verbose_name='تاریخ تولد'
    )
    national_code = models.CharField(
        max_length=10,
        primary_key=True,
        verbose_name='کد ملی',
    )
    file_number = models.IntegerField(
        unique=True,
        verbose_name='شماره پرونده',
    )

    @property
    def سن(self):
        return datetime.now().year - self.birth_day.year

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
            f'{self.national_code} - ' +
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
