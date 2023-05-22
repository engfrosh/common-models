# Generated by Django 4.1.7 on 2023-05-22 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('common_models', '0017_alter_team_scav_tree'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordrole',
            name='secondary_group_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_group', to='auth.group'),
        ),
    ]
