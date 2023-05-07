from django.contrib import admin
from .models import PhoneNumberAbstractUser,PhoneToken
# Register your models here.
class PhoneTokenAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'otp', 'timestamp', 'attempts', 'used')
    search_fields = ('phone_number', )
    list_filter = ('timestamp', 'attempts', 'used')
    readonly_fields = ('phone_number', 'otp', 'timestamp', 'attempts')
admin.site.register(PhoneToken)