# Generated by Django 2.0.2 on 2018-12-04 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0009_auto_20181204_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='المستخدم',
            new_name='user',
        ),
    ]
