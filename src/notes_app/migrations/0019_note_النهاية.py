# Generated by Django 2.0.2 on 2018-12-13 18:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0018_auto_20181213_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='النهاية',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
