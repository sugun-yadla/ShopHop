# Generated by Django 4.2.16 on 2024-12-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shophop', '0002_saveditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.CharField(max_length=100)),
                ('standardized_quantity', models.CharField(max_length=100)),
                ('store', models.CharField(max_length=50)),
            ],
        ),
    ]
