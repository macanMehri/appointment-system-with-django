from django.db import models


GENDER_CHOICES = (
    ('مرد', 'مرد'),
    ('زن', 'زن'),
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
    file_number = models.CharField(
        max_length=100,
        verbose_name='شماره پرونده',
    )
    # TODO: Create a field or property to calculate age

    class Meta:
        verbose_name = 'مراجعه کننده'
        verbose_name_plural = 'مراجعین'

    def __str__(self):
        return (
            f'{self.first_name}' +
            f'{self.last_name}' +
            f'{self.sex}' +
            f'{self.birth_day}' +
            f'{self.national_code}' +
            f'{self.file_number}'
        )
