# Generated by Django 3.0 on 2019-12-21 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='publishing date'),
        ),
    ]
