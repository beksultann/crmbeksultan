# Generated by Django 2.2.2 on 2019-07-22 15:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('counterparties', '0003_auto_20190722_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('phone_number', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('email', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('date_of_birth', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('sex', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('address', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('comment', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('date_of_created', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
