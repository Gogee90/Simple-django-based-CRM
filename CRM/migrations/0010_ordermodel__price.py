# Generated by Django 3.1.7 on 2021-04-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0009_auto_20210411_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
