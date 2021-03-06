# Generated by Django 3.0.3 on 2020-02-25 12:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.datetime.today, null=True, verbose_name='Дата начала курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='courses', to='university.Teacher', verbose_name='Преподаватели'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='current_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.Teacher', verbose_name='Текущий преподаватель'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='end_time',
            field=models.DateTimeField(blank=True, verbose_name='Время окончания занятия'),
        ),
    ]
