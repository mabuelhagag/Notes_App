# Generated by Django 2.0.2 on 2018-12-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20181204_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='الصورة_الشخصية',
            field=models.ImageField(blank=True, upload_to='profile_img'),
        ),
    ]
