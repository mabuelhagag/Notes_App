# Generated by Django 2.0.2 on 2018-12-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0013_note_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='notes-files'),
        ),
        migrations.AlterField(
            model_name='note',
            name='upload_photo',
            field=models.ImageField(blank=True, null=True, upload_to='notes-img'),
        ),
    ]