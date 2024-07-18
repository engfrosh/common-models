# Generated by Django 4.2.14 on 2024-07-18 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0067_alter_userdetails_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='puzzle',
            options={'permissions': [('guess_scavenger_puzzle', 'Can guess for scavenger puzzle'), ('manage_scav', 'Can manage scav'), ('bypass_scav_rules', 'Bypasses all scav rules'), ('lock_scav', 'Can lock scav')], 'verbose_name': 'Scavenger Puzzle', 'verbose_name_plural': 'Scavenger Puzzles'},
        ),
    ]