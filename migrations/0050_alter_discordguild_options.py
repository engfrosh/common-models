# Generated by Django 4.1.7 on 2024-04-28 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0049_alter_facilshift_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discordguild',
            options={'permissions': [('create_role', 'Allows a user to create discord roles'), ('create_channel', 'Allows a user to create discord channels'), ('spirit_on_duty', 'Allows a user to mark themselves as the spirit on duty')], 'verbose_name': 'Discord Guild', 'verbose_name_plural': 'Discord Guilds'},
        ),
    ]