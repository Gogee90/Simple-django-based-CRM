# Generated by Django 3.1.7 on 2021-04-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0012_ordermodel_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='clients',
            field=models.ManyToManyField(blank=True, related_name='clients', to='CRM.ClientsModel'),
        ),
    ]