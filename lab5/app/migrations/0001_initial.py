# Generated by Django 4.0.3 on 2022-03-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('info', models.TextField()),
                ('cost', models.IntegerField(default=0)),
                ('picture', models.ImageField(default='donut-default.jpg', upload_to='donuts/')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
                'db_table': 'Donuts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DonutsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('info', models.TextField()),
                ('picture', models.ImageField(default='donut-default.jpg', upload_to='donuts/')),
                ('fk_donuts', models.ManyToManyField(to='app.donut')),
            ],
            options={
                'verbose_name': 'Car Set',
                'verbose_name_plural': 'Car Sets',
                'db_table': 'DonutsSets',
                'managed': True,
            },
        ),
    ]
