# Generated by Django 4.1.2 on 2023-03-29 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0024_puzzle_stream_branch_puzzlestream_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='stream_branch',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_puzzle', to='common_models.puzzlestream'),
        ),
    ]