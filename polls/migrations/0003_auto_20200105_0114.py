# Generated by Django 3.0 on 2020-01-05 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20191221_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='publish_date',
            field=models.DateTimeField(verbose_name='publishing date'),
        ),
    ]