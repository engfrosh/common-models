# Generated by Django 4.2.14 on 2024-07-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0068_alter_puzzle_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzlestream',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
