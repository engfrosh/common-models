# Generated by Django 4.1 on 2023-04-01 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0010_puzzle_stream_branch_puzzlestream_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='override_nick',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Name Override'),
        ),
    ]
