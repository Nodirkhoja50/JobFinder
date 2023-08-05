from geopy.geocoders import Nominatim

'''class Nominatim:
     def __str__(self,a) -> str:
        pass
a = Nominatim()'''
from work.models import Vacancy
from django.db.models import Case,IntegerField, When, BooleanField,Value
from django.db.models import Q



# Latitude & Longitude input
coordinates = "39.018665, 65.983590"






def check_current_location(coordinates):
    # Initialize Nominatim API
    
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.reverse(coordinates)

        address = location.raw['address']

        # Traverse the data
        city = address.get('city','')
        county = address.get("county",'')
        state = address.get('state', '')
        country = address.get('country', '')
        return state,county
    

print(check_current_location(coordinates))



def filter_by_location(results,state,county):
    state = state.split(' ')[0]
    county = county.split(' ')[0]
    vacancies = results.annotate(
        is_filtered=Case(
            When(Q(city__icontains= state)  & Q(county__icontains=county),then=Value(1)),
            When(Q(city__icontains = state),then=Value(2)),
            #When(Q(specialty='PR')),
            #When(Q(city=city) | Q(county=county)),
            default=Value(3),
            output_field=IntegerField(),
        )
    ).order_by('is_filtered','-city')

    for vacancy in vacancies:
        print(vacancy)
    

    return vacancies


def search_by_location(qs,state,county):
    state = state.split(' ')[0]
    county = county.split(' ')[0]
    vacancies = qs.annotate(
        is_filtered=Case(
            When(Q(city=state) & Q(county=county),then=Value(1)),
            When(Q(city = state), then=Value(2)),
            #When(Q(specialty='PR')),
            #When(Q(city=city) | Q(county=county)),
            default=Value(3),
            output_field=IntegerField(),
        )
    ).order_by('is_filtered','-city')
    return vacancies


def list_by_location(results,specialty,state,county):
    state = state.split(' ')[0]
    county = county.split(' ')[0]
    vacancies = results.annotate(
        is_filtered=Case(
            When(Q(specialty__icontains=specialty) & Q(city__icontains= state) & Q(county__icontains=county),then=Value(1)),
            When(Q(specialty__icontains=specialty),then=Value(2)),
            When(Q(city__icontains = state),then=Value(3)),
            #When(Q(specialty='PR')),
            #When(Q(city=city) | Q(county=county)),
            default=Value(4),
            output_field=IntegerField(),
        )
    ).order_by('is_filtered','specialty','-city')

    for vacancy in vacancies:
        print(vacancy)
    

    return vacancies