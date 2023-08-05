from django.contrib import admin
from .models import Vacancy
# Register your models here.
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'slug','owner', 'specialty', 'city','created_at']
    list_filter = ['specialty', 'city', 'created_at', 'owner']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['owner']
    #date_hierarchy = 'publish'
    ordering = ['-created_at']


admin.site.register(Vacancy,VacancyAdmin)