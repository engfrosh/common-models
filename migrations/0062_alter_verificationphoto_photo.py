# Generated by Django 4.1.13 on 2024-06-23 00:25

import common_models.scav_models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0061_alter_faqpage_restricted_alter_puzzle_stream_puzzle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationphoto',
            name='photo',
            field=models.ImageField(null=True, upload_to=common_models.scav_models._puzzle_verification_photo_upload_path),
        ),
    ]
