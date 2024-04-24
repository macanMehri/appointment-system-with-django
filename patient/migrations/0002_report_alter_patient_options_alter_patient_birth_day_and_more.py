# Generated by Django 4.2 on 2024-04-24 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر داده شده')),
                ('title', models.CharField(max_length=255, verbose_name='تیتر')),
                ('description', models.TextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'گزارش',
                'verbose_name_plural': 'گزارشات',
            },
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'مراجعه کننده', 'verbose_name_plural': 'مراجعین'},
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_day',
            field=models.DateField(verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='file_number',
            field=models.CharField(max_length=100, verbose_name='شماره پرونده'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='national_code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('مرد', 'مرد'), ('زن', 'زن')], default='مرد', max_length=9, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر داده شده'),
        ),
        migrations.CreateModel(
            name='PatientsReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر داده شده')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient', verbose_name='مراجعه کننده')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.report', verbose_name='گزارش')),
            ],
            options={
                'verbose_name': 'گزارش مراجعه کننده',
                'verbose_name_plural': 'گزارشات مراجعه کننده',
            },
        ),
    ]