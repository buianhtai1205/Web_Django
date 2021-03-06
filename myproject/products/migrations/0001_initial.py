# Generated by Django 4.0.3 on 2022-04-24 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.FloatField()),
                ('display', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('main_camera', models.CharField(max_length=50)),
                ('selfie_camera', models.CharField(max_length=50)),
                ('chip', models.CharField(max_length=50)),
                ('RAM', models.CharField(max_length=50)),
                ('ROM', models.CharField(max_length=50)),
                ('sim', models.CharField(max_length=50)),
                ('battery', models.CharField(max_length=50)),
                ('manufacturer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturers.manufacturer')),
            ],
        ),
    ]
