# Generated by Django 4.1.7 on 2023-07-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0028_facilshift_end_facilshift_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='free_hints',
            field=models.IntegerField(default=0),
        ),
    ]