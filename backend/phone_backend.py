import datetime
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from core.models import PhoneToken
from core.utils import model_field_attr

from django.utils import timezone
from django.conf import settings
import pytz
# Get the current time in the 'Asia/Tashkent' time zone
uzbekistan_tz = pytz.timezone('Asia/Tashkent')
current_time = timezone.now().astimezone(uzbekistan_tz)

class PhoneBackend(ModelBackend):
    def __init__(self, *args, **kwargs):
        
        self.user_model = get_user_model()

    def get_phone_number_data(self, phone_number):
        """
        Method used for filtering query.
        """
        phone_number_field = getattr(settings, 'PHONE_NUMBER_FIELD', 'phone_number')
        data = {
            phone_number_field: phone_number
        }
        return data

    def get_username(self):
        """
        Returns a UUID-based 'random' and unique username.

        This is required data for user models with a username field.
        """
        return str(uuid.uuid4())[:model_field_attr(
            self.user_model, 'username', 'max_length')]

    def create_user(self, phone_token, **extra_fields):
        """
        Create and returns the user based on the phone_token.
        """
        password = self.user_model.objects.make_random_password()

        username = extra_fields.get('username', self.get_username())
        password = extra_fields.get('password', password)
        kwargs = {
            'username': username,
            'password': password,
        }
        
        
        phone_number = phone_token.phone_number
        kwargs.update(self.get_phone_number_data(phone_number))
        user = self.user_model.objects.create_user(**kwargs)
        #print("this is kwarg",kwargs)
        #print("this is user",user)
        return user

    def authenticate(self, request, pk=None, otp=None, **extra_fields):
        if pk is None:
            return

        # 1. Validating the PhoneToken with PK and OTP.
        # 2. Check if phone_token and otp are same, within the given time range
        timestamp_difference = current_time - datetime.timedelta(
            minutes=getattr(settings, 'PHONE_LOGIN_MINUTES', 10)
        )
        try:

            phone_token = PhoneToken.objects.get(
                pk=pk,
                otp=otp,
                used=False,
                timestamp__gte=timestamp_difference
            )
        except PhoneToken.DoesNotExist:
            phone_token = PhoneToken.objects.get(pk=pk)
            phone_token.attamps = phone_token.attamps + 1
            phone_token.save()
            raise PhoneToken.DoesNotExist

        # 3. Create new user if he doesn't exist. But, if he exists login.
        
        user = self.user_model.objects.filter(
            **self.get_phone_number_data(phone_token.phone_number)
        ).first()

        if not user:
            user = self.create_user(
                phone_token=phone_token,
                **extra_fields
            )
        phone_token.used = True
        phone_token.attamps += 1
        phone_token.save()
        return user