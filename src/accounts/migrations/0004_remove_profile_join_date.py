# Generated by Django 2.0.2 on 2018-12-02 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181202_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='join_date',
        ),
    ]