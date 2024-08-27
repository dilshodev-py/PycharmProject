# Generated by Django 5.0.6 on 2024-07-05 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_vacancy_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='apps.company'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='namee'),
            preserve_default=False,
        ),
    ]