# Generated by Django 3.0 on 2020-01-05 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumbs_down',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbs_up',
        ),
    ]
