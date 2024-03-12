# Generated by Django 4.2.11 on 2024-03-12 20:41

from django.db import migrations, models
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0039_userdetails_charter'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Page ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LockoutPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', django_unixdatetimefield.fields.UnixDateTimeField()),
                ('end', django_unixdatetimefield.fields.UnixDateTimeField()),
            ],
        ),
    ]
