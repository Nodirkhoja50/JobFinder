from work.models import Vacancy
from django.db.models import Case,IntegerField, When, BooleanField,Value
from django.db.models import Q
'''vacancies = Vacancy.objects.annotate(
    is_filtered=Case(
        When(Q(city='Qashqadaryo') | Q(county='chilonzor'), then=True),
        default=False,
        output_field=BooleanField()
    )
).order_by('-is_filtered', '-city', '-county')'''



vacancies = Vacancy.objects.annotate(
    is_filtered=Case(
        When(Q(city='toshkent', county='chilonzor')),
        When(Q(city='toshkent') | Q(county='chilonzor')),
        default=Value(3),
        output_field=IntegerField(),
    )
).order_by('is_filtered','city', 'county')

for vacancy in vacancies:
    print(vacancy)