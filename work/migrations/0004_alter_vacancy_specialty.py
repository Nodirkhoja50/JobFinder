# Generated by Django 4.2.1 on 2023-08-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_alter_vacancy_from_salary_alter_vacancy_to_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='specialty',
            field=models.CharField(choices=[('LO', 'Logistika'), ('CR', 'Kuryer'), ('PR', 'Dasturchi'), ('DV', 'Haydovchi'), ('DR', 'Direktor'), ('SM', 'Sotuvchi'), ('SU', 'Nazoratchi'), ('SE', 'Tikuvchi'), ('MR', 'Menejer'), ('CI', 'Kassir'), ('EG', 'Muhandis'), ('WA', 'Ofisiant'), ('OR', 'Operator'), ('AD', 'Administrator'), ('CL', 'Tozalovchi'), ('LW', 'Huquqshunos'), ('AS', 'Yordamchi'), ('BU', 'Quruvchi'), ('AM', 'Boshqaruvchi yordamchisi'), ('DE', 'Dizayner'), ('WD', 'Payvandchi'), ('AC', 'Buxgalter'), ('SK', "Do'kondor"), ('SC', 'Secretary'), ('LD', 'Yuklovchi'), ('EL', 'Elektrchi'), ('CO', 'Oshpaz'), ('EC', 'Iqtisodchi'), ('ME', 'Merchandiser'), ('SA', 'Tizim Administratori'), ('TO', 'Turist')], max_length=2),
        ),
    ]
