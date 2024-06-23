# Generated by Django 4.2 on 2024-06-11 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_doctor_alter_patient_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='service',
        ),
        migrations.CreateModel(
            name='DoctorsServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر داده شده')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.doctor', verbose_name='پزشک')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.service', verbose_name='خدمت')),
            ],
            options={
                'verbose_name': 'خدمت پزشک',
                'verbose_name_plural': 'خدمات پزشک',
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='doctor_and_service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='patient.doctorsservices', verbose_name='خدمات و پزشک'),
            preserve_default=False,
        ),
    ]