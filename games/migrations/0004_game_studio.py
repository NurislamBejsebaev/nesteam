# Generated by Django 4.1.7 on 2023-08-16 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_genre_game_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='games.studio'),
        ),
    ]
