# Generated by Django 4.1.7 on 2024-04-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0047_remove_puzzle_qr_code_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilshiftsignup',
            name='attendance',
            field=models.BooleanField(default=False),
        ),
    ]