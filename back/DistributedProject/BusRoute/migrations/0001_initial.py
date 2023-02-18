# Generated by Django 4.1.5 on 2023-02-16 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Bus',
            },
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=52)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11)),
            ],
            options={
                'verbose_name_plural': 'BusStop',
            },
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusRoute.bus')),
                ('busStop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusRoute.busstop')),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusRoute.timetable')),
            ],
            options={
                'verbose_name_plural': 'Routes',
            },
        ),
    ]