# Generated by Django 3.1.1 on 2020-10-22 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_user_enc_pswd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='VIN',
        ),
    ]
