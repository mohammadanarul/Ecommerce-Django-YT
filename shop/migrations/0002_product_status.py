# Generated by Django 4.0 on 2022-03-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('SALE', 'SALE'), ('HOT', 'HOT')], default='NEW', max_length=5),
            preserve_default=False,
        ),
    ]
