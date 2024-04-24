# Generated by Django 4.2 on 2024-04-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_patientsreports_medicine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='medicine_count',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='medicine_description',
        ),
        migrations.AddField(
            model_name='patientsreports',
            name='medicine_count',
            field=models.IntegerField(default=1, verbose_name='تعداد مورد نیاز'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientsreports',
            name='medicine_description',
            field=models.TextField(default=2, verbose_name='طریقه مصرف'),
            preserve_default=False,
        ),
    ]
