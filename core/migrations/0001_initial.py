# Generated by Django 4.2.1 on 2023-05-07 12:12

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(editable=False, max_length=128, region=None)),
                ('otp', models.CharField(editable=False, max_length=40)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('attamps', models.IntegerField(default=0)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'OTP Token',
                'verbose_name_plural': 'OTP Tokens',
            },
        ),
    ]
