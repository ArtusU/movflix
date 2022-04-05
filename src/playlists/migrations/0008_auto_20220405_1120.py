# Generated by Django 3.2.12 on 2022-04-05 10:20

from django.db import migrations, models
import django.db.models.deletion
import playlists.models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0007_playlist_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaylistRelated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist')),
                ('related', models.ForeignKey(limit_choices_to=playlists.models.pr_limit_choices_to, on_delete=django.db.models.deletion.CASCADE, related_name='related_item', to='playlists.playlist')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='related',
            field=models.ManyToManyField(blank=True, related_name='_playlists_playlist_related_+', through='playlists.PlaylistRelated', to='playlists.Playlist'),
        ),
    ]
