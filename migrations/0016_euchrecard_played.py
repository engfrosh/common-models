# Generated by Django 4.1 on 2023-01-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0015_remove_euchrecard_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='euchrecard',
            name='played',
            field=models.BooleanField(default=False, verbose_name='Played'),
        ),
    ]
