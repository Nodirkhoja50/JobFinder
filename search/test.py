from geopy.geocoders import Nominatim


from work.models import Vacancy
from django.db.models import Case,IntegerField, When, BooleanField,Value
from django.db.models import Q



# Latitude & Longitude input
coordinates = "42.677889, 63.135119"


geolocator = Nominatim(user_agent="MyApp")
location = geolocator.reverse(coordinates)

address = location.raw['address']

#street = address.get('street', '')
city = address.get('city','')
county = address.get('county', '')
state = address.get('state', '')
country = address.get('country', '')

print(state,county)



def filter_by_location(specialty,city,county):
    city = city.split(' ')[0]
    county = county.split(' ')[0]
    print(city,county)
    vacancies = Vacancy.objects.annotate(
        is_filtered=Case(
            When(Q(city__icontains = city) & Q(specialty=specialty) & Q(county__icontains=county),then=Value(1)),
            When(Q(specialty=specialty), then=Value(2)),
            When(Q(city__icontains = city),then=Value(3)),
            #When(Q(specialty='PR')),
            #When(Q(city=city) | Q(county=county)),
            default=Value(4),
            output_field=IntegerField(),
        )
    ).order_by('is_filtered','specialty' ,'-city')

    for vacancy in vacancies:
        print(vacancy)
    

    return vacancies

filter_by_location('PR','Qashqadaryo viloyati','olmazor tumani')
