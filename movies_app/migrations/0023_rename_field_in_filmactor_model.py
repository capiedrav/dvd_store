# Generated by Django 3.2.13 on 2022-12-12 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0022_remove_unnecessary_fields_from_filmactor_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmactor',
            old_name='actor_new',
            new_name='actor',
        ),
        migrations.AlterUniqueTogether(
            name='filmactor',
            unique_together={('actor', 'film')},
        ),
    ]
