# Generated by Django 4.2.6 on 2023-11-07 10:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0002_arraydjango'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arraydjango',
            name='serena',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), size=None), size=None),
        ),
    ]