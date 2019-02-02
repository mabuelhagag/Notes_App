# Generated by Django 2.0.2 on 2019-01-31 09:35

from django.db import migrations, models
import django.db.models.deletion
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0021_auto_20190130_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('module', models.CharField(choices=[('ELE', 'Electronics'), ('ARD', 'Arduino'), ('CAD', 'Computer-aided Design'), ('LAS', 'Laser-cutting'), ('THD', '3D Printing'), ('FIN', 'Final Project')], max_length=3)),
                ('title', django_bleach.models.BleachField(max_length=255)),
                ('text', django_bleach.models.BleachField(null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='note',
            name='circuit',
        ),
        migrations.RemoveField(
            model_name='note',
            name='circuit_problem',
        ),
        migrations.RemoveField(
            model_name='note',
            name='circuit_schema',
        ),
        migrations.AddField(
            model_name='step',
            name='documentation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes_app.Note'),
        ),
    ]