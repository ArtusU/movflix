# Generated by Django 3.2.12 on 2022-03-24 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0002_auto_20220324_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVShowProxy',
            fields=[
            ],
            options={
                'verbose_name': 'TV Show',
                'verbose_name_plural': 'TV Shows',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('playlists.playlist',),
        ),
        migrations.CreateModel(
            name='TVShowSeasonProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('playlists.playlist',),
        ),
    ]
