# Generated by Django 2.2.2 on 2019-07-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_cart_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='Image_of_products/foto.png', upload_to='Image_of_products'),
        ),
    ]