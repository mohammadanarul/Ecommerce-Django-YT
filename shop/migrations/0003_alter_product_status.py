# Generated by Django 4.0 on 2022-03-04 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('NONE', 'NONE'), ('NEW', 'NEW'), ('SALE', 'SALE'), ('HOT', 'HOT')], default='NONE', max_length=5),
        ),
    ]
