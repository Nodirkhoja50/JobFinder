from django.contrib import admin
from .models import PhoneNumberAbstractUser,PhoneToken
# Register your models here.
class PhoneTokenAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number','username','last_login', 'otp','attamps','timestamp', 'used')
    search_fields = ('phone_number', )
    list_filter = ('timestamp', 'attamps', 'used')
admin.site.register(PhoneToken,PhoneTokenAdmin)

class PhoneAbstractUser(admin.ModelAdmin):
    list_display = ('id','phone_number','username','last_login',"is_staff")
    search_fields = ('phone_number', )
admin.site.register(PhoneNumberAbstractUser,PhoneAbstractUser)
#admin.site.register(PhoneNumberAbstractUser)