# Generated by Django 2.2.2 on 2019-07-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opened_cash', models.DateTimeField(auto_now_add=True)),
                ('closed_cash', models.DateTimeField(blank=True, null=True)),
                ('cashier', models.CharField(blank=True, max_length=30, null=True)),
                ('cash', models.CharField(blank=True, max_length=30, null=True)),
                ('shop', models.CharField(blank=True, max_length=30, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_sold_product', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
