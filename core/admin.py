from django.contrib import admin
from .models import PhoneNumberAbstractUser,PhoneToken
# Register your models here.
class PhoneTokenAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number','last_login', 'otp','attamps', 'used')
    search_fields = ('phone_number', )
    list_filter = ('timestamp', 'attamps', 'used')
admin.site.register(PhoneToken,PhoneTokenAdmin)
#admin.site.register(PhoneNumberAbstractUser)