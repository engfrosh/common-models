# Generated by Django 4.1.2 on 2023-03-29 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0023_alter_puzzle_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='stream_branch',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_puzzle', to='common_models.puzzlestream'),
        ),
        migrations.AddField(
            model_name='puzzlestream',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]
