# Generated by Django 2.1.5 on 2022-03-19 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('movie_id', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]