# Generated by Django 5.0.4 on 2024-07-18 14:05

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedOrder',
            fields=[
            ],
            options={
                'verbose_name': 'Archived Order',
                'verbose_name_plural': 'Archived Orders',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='BeingDeliveredOrder',
            fields=[
            ],
            options={
                'verbose_name': 'Being Delivered Order',
                'verbose_name_plural': 'Being Delivered Orders',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='CanceledOrder',
            fields=[
            ],
            options={
                'verbose_name': 'Canceled Order',
                'verbose_name_plural': 'Canceled Orders',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='DeliveredOrder',
            fields=[
            ],
            options={
                'verbose_name': 'Delivered Order',
                'verbose_name_plural': 'Delivered Orders',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='NewOrder',
            fields=[
            ],
            options={
                'verbose_name': 'New Order',
                'verbose_name_plural': 'New Orders',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='NotPickUpPhoneOrder',
            fields=[
            ],
            options={
                'verbose_name': 'Not Pick Up Phone Order',
                'verbose_name_plural': 'Not Pick Up Phone Orders',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
        migrations.CreateModel(
            name='ReadyToStartOrder',
            fields=[
            ],
            options={
                'verbose_name': 'Ready To Start Order',
                'verbose_name_plural': 'Ready To Start Orders',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apps.order',),
        ),
    ]