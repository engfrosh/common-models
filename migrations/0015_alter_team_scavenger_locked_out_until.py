# Generated by Django 4.0.6 on 2022-08-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0014_alter_team_scavenger_locked_out_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='scavenger_locked_out_until',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
