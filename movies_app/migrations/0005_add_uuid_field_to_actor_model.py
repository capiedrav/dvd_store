# Generated by Django 3.2.13 on 2022-12-06 22:55

from django.db import migrations, models
import uuid


def populate_actor_uuid(apps, schema_editor):

    Actor = apps.get_model("movies_app", "Actor")

    # populate actor_uuid field
    for actor in Actor.objects.all():
        actor.actor_uuid = uuid.uuid4()
        actor.save()


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0004_add_auto_now_to_last_update_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='filmactor',
            options={'managed': True, 'verbose_name_plural': 'Film Actors'},
        ),
        migrations.AlterModelOptions(
            name='filmcategory',
            options={'managed': True, 'verbose_name_plural': 'Film Categories'},
        ),
        migrations.AlterModelOptions(
            name='filmtext',
            options={'managed': True, 'verbose_name_plural': 'Film Texts'},
        ),
        migrations.AddField(
            model_name='actor',
            name='actor_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),

        # populate actor_uuid field
        migrations.RunPython(populate_actor_uuid, reverse_code=migrations.RunPython.noop),

        # then change null field to false, to prevent new null entries in the database
        migrations.AlterField(
            model_name='actor',
            name='actor_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=False, unique=True),
        ),
    ]