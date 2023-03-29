# Generated by Django 4.1 on 2023-02-10 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common_models', '0004_alter_userdetails_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordMessage',
            fields=[
                ('type', models.CharField(max_length=64, verbose_name='Type')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Channel ID')),
            ],
        ),
        migrations.CreateModel(
            name='PronounOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emote', models.CharField(max_length=64, unique=True, verbose_name='Emote')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
            ],
        ),
        migrations.AlterModelOptions(
            name='userdetails',
            options={'permissions': [('check_in', 'Can manage user check in')], 'verbose_name': 'User Details', 'verbose_name_plural': "Users' Details"},
        ),
        migrations.AddField(
            model_name='userdetails',
            name='override_nick',
            field=models.CharField(blank=True, max_length=64, verbose_name='Name Override'),
        ),
        migrations.CreateModel(
            name='Pronoun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Pronoun')),
                ('order', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'order')},
            },
        ),
    ]
