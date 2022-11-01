# Generated by Django 3.2.13 on 2022-10-19 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0012_populate_customer_foreign_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='active',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='customer_old',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='staff_old',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='active',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='email',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='password',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='username',
        ),
        migrations.RemoveField(
            model_name='store',
            name='manager_staff_old',
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store_app.customer'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store_app.staff'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store_app.customer'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store_app.staff'),
        ),
        migrations.AlterUniqueTogether(
            name='rental',
            unique_together={('rental_date', 'inventory', 'customer')},
        ),
        migrations.RemoveField(
            model_name='rental',
            name='customer_old',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='staff_old',
        ),
    ]