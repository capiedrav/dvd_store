# Generated by Django 3.2.13 on 2022-10-17 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial_and_workaround_foreign_key_bug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='rental',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'managed': True},
        ),
    ]
