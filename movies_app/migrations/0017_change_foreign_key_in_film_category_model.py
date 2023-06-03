# Generated by Django 3.2.13 on 2022-12-11 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0016_populate_film_field_of_filmactor_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmcategory',
            name='film',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to='movies_app.film'),
        ),
        migrations.AlterField(
            model_name='filmcategory',
            name='film_old',
            field=models.IntegerField(),
        ),
    ]