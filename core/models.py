from __future__ import unicode_literals
from django.db import models
import datetime
import os
import re
import hashlib
from django.conf import settings
from django.contrib import auth
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,AbstractUser,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from eskiz_sms import EskizSMS
from django.contrib.auth.models import User
from specialty.models import Specialty
#from work.models import Vacancy
eskiz = EskizSMS(email=getattr(settings,"ESKIZ_EMAIL"),password=getattr(settings,"ESKIZ_PASSWORD"))


# Create your models here.
class UserManager(BaseUserManager):
    def create_superuser(self,username,phone_number,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned is_staff=True') 
        return self.create_user(username,phone_number,password,**other_fields)
    

    def create_user(self,username,phone_number,password,**other_fields):
        if not username:
            raise ValueError('username must be assigned')
        user  = self.model(
            username = username,
            phone_number = phone_number,
            **other_fields
        )
        
        user.set_password(password)
        user.save(using = self._db)
        return user
    
class PhoneNumberAbstractUser(AbstractBaseUser,PermissionsMixin):
    phone_number = PhoneNumberField(unique = True)
    username = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    specialty = models.CharField(max_length=2,
                                choices=Specialty.Uz_Status.choices,
                                blank=True)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    tg_username = models.URLField(max_length=200)
    favorites = models.ManyToManyField('work.Vacancy', related_name='favorited_by')
    objects = UserManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def __str__(self) -> str:
        return f'{self.username}'
    
class PhoneToken(models.Model):
    phone_number = PhoneNumberField(editable = False)
    username = models.CharField(max_length=50)
    otp = models.CharField(max_length=42,editable=False)
    timestamp = models.DateTimeField(auto_now_add=True,editable=False)
    last_login = models.DateField(auto_now=True)
    attamps = models.IntegerField(default=0)
    used = models.BooleanField(default=False)
    test=models.CharField(max_length=23)

    class Meta:
        verbose_name = "OTP Token"
        verbose_name_plural = "OTP Tokens"

    def __str__(self) -> str:
        return f'{self.phone_number}-{self.otp}'
    
    @classmethod
    def create_otp_for_numbers(cls,number):
        #i am going to take start time

        today_min = datetime.datetime.combine(datetime.date.today(),datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(),datetime.time.max)
        otp = cls.objects.filter(phone_number = number,timestamp__range = (today_min,today_max))
        if otp.count() <= getattr(settings,'PHONE_LOGIN_ATTEMPTS',10):
            otp = cls.generate_otp(length = getattr(settings,'PHONE_LOGIN_OTP_LENGTH',6))
            phone_token = PhoneToken(phone_number = number,otp=otp)
            phone_token.save()

            sms_body=render_to_string(
                "otp.txt",
                {"otp":otp}
            )

            #eskiz.send_sms(number,sms_body,from_whom = '4546',callback_url=None)
            return phone_token
        else:
            return False
    @classmethod
    def generate_otp(cls,length=6):
        hash_algorithm = getattr(settings,"PHONE_LOGIN_OTP_HASH_ALGORITHM","sha256")
        m=getattr(hashlib,hash_algorithm)()
        m.update(getattr(settings,'SECRET_KEY',None).encode('utf-8'))
        m.update(os.urandom(16))
        otp = str(int(m.hexdigest(),16))[-length:]
        return otp


