# Generated by Django 4.2.1 on 2023-06-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='city',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='county',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]