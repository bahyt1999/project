# Generated by Django 4.1 on 2023-01-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0002_product_balls_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='final_payment',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='balls',
            field=models.FloatField(default=True),
        ),
    ]
