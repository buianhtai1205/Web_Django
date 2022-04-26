# Generated by Django 4.0.3 on 2022-04-26 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0002_alter_manufacturer_image'),
        ('products', '0002_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturers.manufacturer', verbose_name='Manafacturer'),
        ),
    ]
