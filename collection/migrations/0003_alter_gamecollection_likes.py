# Generated by Django 4.1.7 on 2023-09-14 04:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0002_alter_gamecollection_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamecollection',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_collection', to=settings.AUTH_USER_MODEL),
        ),
    ]
