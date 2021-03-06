# Generated by Django 2.2.2 on 2019-07-21 17:03

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20190721_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='vat',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
    ]
