# Generated by Django 3.2.13 on 2022-12-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0014_add_auto_now_to_last_update_fields'),
        ("movies_app", "0010_add_uuid_field_to_film_model"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'managed': True, 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'managed': True, 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'managed': True, 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': True, 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'managed': True, 'verbose_name_plural': 'Inventory'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'managed': True, 'verbose_name_plural': 'Staff'},
        ),
        migrations.AlterField(
            model_name='inventory',
            name='film',
            field=models.IntegerField(),
        ),
    ]