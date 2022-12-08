# Generated by Django 3.2.13 on 2022-12-06 23:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0006_change_one_to_one_actor_in_film_actor_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='actor_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='actor',
            name='actor_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
