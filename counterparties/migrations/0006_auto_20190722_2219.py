# Generated by Django 2.2.2 on 2019-07-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counterparties', '0005_employees_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='pay',
            field=models.IntegerField(default=0),
        ),
    ]
