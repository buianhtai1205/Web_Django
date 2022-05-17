# Generated by Django 4.0.3 on 2022-05-17 07:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image'),
        ('customers', '0004_alter_customer_token_remove_order_product_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='token',
            field=models.CharField(blank=True, default=uuid.UUID('d03d15fe-ee75-48dc-be42-f9ca0cfd1284'), editable=False, max_length=200),
        ),
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.ManyToManyField(through='customers.Order_Product', to='products.product'),
        ),
    ]
