# Generated by Django 4.0.6 on 2022-08-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0015_alter_team_scavenger_locked_out_until'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teampuzzleactivity',
            options={'verbose_name': 'Team Puzzle Activity', 'verbose_name_plural': 'Team Puzzle Activities'},
        ),
        migrations.AddField(
            model_name='puzzle',
            name='secret_id',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teampuzzleactivity',
            name='locked_out_until',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='teampuzzleactivity',
            name='puzzle_completed_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
