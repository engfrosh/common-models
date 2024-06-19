# Generated by Django 4.1.13 on 2024-06-09 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('common_models', '0055_remove_faqpage_restricted_faqpage_restricted_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqpage',
            name='restricted_group',
        ),
        migrations.AddField(
            model_name='faqpage',
            name='restricted',
            field=models.ManyToManyField(to='auth.group'),
        ),
    ]