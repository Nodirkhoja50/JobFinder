from django.db import models
from django.conf import settings
from core.models import PhoneNumberAbstractUser
from django.db import transaction
from django.db.models import Q
from .validators import validate_salary
from .converter import converter_to_usd
Owner = settings.AUTH_USER_MODEL
class VacancyQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(is_public = True)

    def search(self,query,owner=None):

        lookup = Q(title__icontains = query) | Q(description__icontains=query)
        qs = self.is_public().filter(lookup)
        if owner is not None:
            qs2 = self.filter(owner = owner).filter(lookup)
            #qs = (qs | qs2).distinct()
        return qs
    

class VacancyManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return VacancyQuerySet(self.model,using=self._db)

    def search(self,query,owner = None):
        return self.get_queryset().search(query,owner)


class Vacancy(models.Model):
    owner = models.ForeignKey(PhoneNumberAbstractUser,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50,blank=False)
    company_name = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=30)
    description = models.TextField()
    salary = models.CharField(max_length=50,blank=False,default=0)
    bargain = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    tg_contact = models.CharField(max_length=50,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    objects = VacancyManager()
    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancy"

    def __str__(self) -> str:
        return f"{self.city}-{self.county}" 
    
    @classmethod
    def update_is_public(cls,elm):
        with transaction.atomic():
            vacancy = Vacancy.objects.filter(id = elm["id"]).first()
            vacancy.is_public = elm["is_public"]
            vacancy.save()

                #Vacancy.objects.update(**elm)


    @classmethod
    def is_negotiable(cls,salary,barging):

        if barging:
            salary = "negotiable"
            return salary
        
        if salary != 0:
            value = validate_salary(salary)
            salary = converter_to_usd(value)
            return salary
        return None


