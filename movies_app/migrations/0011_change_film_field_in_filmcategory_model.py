# Generated by Django 3.2.13 on 2022-12-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0010_add_uuid_field_to_film_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmactor',
            name='film',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filmcategory',
            name='film',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]