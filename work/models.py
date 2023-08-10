from django.db import models
from django.conf import settings
from core.models import PhoneNumberAbstractUser
from django.db import transaction
from django.db.models import Q
from .validators import validate_salary
#from .converter import converter_to_usd
from django.db.models import Case,IntegerField, When, BooleanField,Value
from django.db.models import Q
from specialty.models import Specialty
from rest_framework.reverse import reverse
Owner = settings.AUTH_USER_MODEL
class VacancyQuerySet(models.QuerySet):

    def get_by_location(self,city,county):
        vacancies = Vacancy.objects.annotate(
        is_filtered=Case(
            When(Q(city= city) & Q(county=county),then=Value(1)),
            When(Q(city=city), then=Value(2)),
            default=Value(3),
            output_field=IntegerField(),
        )
    ).order_by('is_filtered','-city')
        return vacancies
    #check is publick or not
    def is_public(self):
        return self.filter(is_public = True)
    
    #bring all specialty
    def specialty(self,specialty):
        return self.is_public().filter(specialty = specialty)

    #search all jobs
    def search(self,query,owner=None):

        lookup = Q(title__icontains = query) | Q(description__icontains=query)
        qs = self.is_public().filter(lookup)

        if owner is not None:
            qs2 = self.filter(owner = owner).filter(lookup)
            #qs = (qs | qs2).distinct()
        return qs
    
    #choose specialty 
    def search_by_specialty(self,key,owner = None):
        lookup = Q(specialty = key)
        qs = self.is_public().filter(lookup)

        if owner is not None:
            qs2 = self.filter(owner=owner).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs
    
    def search_inside_specialty(self,query,specialty,owner = None):
        lookup = Q(title__icontains = query) | Q(description__icontains=query)
        qs = self.specialty(specialty).filter(lookup)

        if owner is not None:
            qs2 = self.filter(owner=owner).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


    def list_by_public(self,owner=None):
        qs = self.is_public().all()
        if owner is not None:
            qs2 = self.filter(owner=owner).all()
            qs = (qs | qs2).distinct()
        return qs
    


class VacancyManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return VacancyQuerySet(self.model,using=self._db)

    def search(self,query,owner = None):
        return self.get_queryset().search(query,owner)




class Vacancy(models.Model):
    class Currency(models.TextChoices):
        dollar = 'do','$'
        sum = 'sm','сум'
    owner = models.ForeignKey(PhoneNumberAbstractUser,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50,blank=False)
    slug = models.SlugField(max_length=250,unique=False)
    specialty = models.CharField(max_length=2,
                                choices=Specialty.Uz_Status.choices,
                                blank=False)
    company_name = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=30)
    description = models.TextField()
    favorites = models.ManyToManyField(PhoneNumberAbstractUser, related_name='favorited_by')
    currency = models.CharField(max_length=2,choices=Currency.choices,default=Currency.sum,blank=False)
    from_salary = models.IntegerField(default=0,blank=False)
    to_salary = models.IntegerField(default=0,blank=True)
    bargain = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    tg_contact = models.CharField(max_length=50,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    objects = VacancyManager()
    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancy"
    
    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title'])
        ]

    def __str__(self) -> str:
        return f"{self.city}-{self.county}-{self.specialty}" 
    
    def get_absolute_url(self):
            return reverse('work:detial',
                           args=[self.slug,
                           self.pk])
    
    '''def get_from_salary(self):
        return int(self.from_salary)
    
    def get_to_salary(self):
        return int(self.to_salary)'''

    @classmethod
    def update_is_public(cls,elm):
        with transaction.atomic():
            vacancy = Vacancy.objects.filter(id = elm["id"]).first()
            vacancy.is_public = elm["is_public"]
            vacancy.save()

                #Vacancy.objects.update(**elm)


    '''@classmethod
    def is_negotiable(cls,salary,barging):

        if barging:
            salary = "negotiable"
            return salary
        
        if salary != 0:
            value = validate_salary(salary)
            salary = converter_to_usd(value)
            return salary
        return None'''


