# Generated by Django 3.2.12 on 2022-03-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
