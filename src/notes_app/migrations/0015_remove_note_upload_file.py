# Generated by Django 2.0.2 on 2018-12-09 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0014_auto_20181209_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='upload_file',
        ),
    ]