# Generated by Django 4.2.16 on 2024-12-05 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shophop', '0005_alter_product_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='productData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
    ]
