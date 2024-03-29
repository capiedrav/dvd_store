# Generated by Django 3.2.13 on 2022-12-11 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0013_rename_film_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmactor',
            name='film',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='movies_app.film'),
        ),
        migrations.AddField(
            model_name='filmcategory',
            name='film',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='movies_app.film'),
        ),
    ]
