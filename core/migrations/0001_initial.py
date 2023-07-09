# Generated by Django 4.2.1 on 2023-06-24 10:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(editable=False, max_length=128, region=None)),
                ('username', models.CharField(max_length=50)),
                ('otp', models.CharField(editable=False, max_length=42)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('attamps', models.IntegerField(default=0)),
                ('used', models.BooleanField(default=False)),
                ('test', models.CharField(max_length=23)),
            ],
            options={
                'verbose_name': 'OTP Token',
                'verbose_name_plural': 'OTP Tokens',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumberAbstractUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
