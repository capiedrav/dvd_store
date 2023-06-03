# Generated by Django 3.2.13 on 2022-12-11 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0012_change_primary_key_of_film_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmactor',
            old_name='film',
            new_name='film_old',
        ),
        migrations.RenameField(
            model_name='filmcategory',
            old_name='film',
            new_name='film_old',
        ),
        migrations.AlterUniqueTogether(
            name='filmcategory',
            unique_together={('film_old', 'category')},
        ),
    ]