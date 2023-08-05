from django.db import models
from django.db.models import Q
# Create your models here.
class Specialty(models.Model):
    class Status(models.TextChoices):
        Courier = "CR","Courier"
        Driver  = "DV","Driver"
        Salesman = "SM","Salesman"
        Cashier = "CI","Cashier"
        Administrator = "AD","Administrator"
        Operator = "OR", "Operator"
        Programmer = "PR","Programmer"
        Manager = "MR" , "Manager"
        Assistant = "AS","Assistant"
        Builder = "BU","Builder"
        Assistant_Manager = "AM","Assistant Manager"
        Welder = "WD","Welder"
        Accountant = "AC","Accountant"
        Engineer = "EG","Engineer"
        Director = "DR","Director"
        Storekeeper = "SK","Storekeeper"
        Secretary = "SC","Secretary"
        Lawyer = "LW","Lawyer"
        Loader = "LD","Loader"
        Cleaner = "CL","Cleaner"
        Designer = "DE","Designer"
        Electrician ="EL","Electrician"
        Cook = 'CO','Cook'
        Economist ='EC','Economist'
        Merchandiser = 'ME','Merchandiser'
        System_Administrator = 'SA','System_Administrator'
        Waiter = 'WA','Waiter'
        Supervisor = 'SU','Supervisor'

    class Uz_Status(models.TextChoices):
        Logistika = 'LO','Logistika'
        Courier = 'CR','Kuryer'
        Programmer = "PR","Dasturchi"
        Driver  = 'DV','Haydovchi'
        Director = "DR","Direktor"
        Salesman = "SM","Sotuvchi"
        Supervisor = 'SU','Nazoratchi'
        Seamstress = 'SE','Tikuvchi'
        Manager = "MR" , "Menejer"
        Cashier = "CI","Kassir"
        Engineer = "EG","Muhandis"
        Waiter = 'WA','Ofisiant'
        Operator = "OR", "Operator"
        Administrator = "AD","Administrator"
        Cleaner = "CL","Tozalovchi"
        Lawyer = "LW","Huquqshunos"
        Assistant = "AS","Yordamchi"
        Builder = "BU","Quruvchi"
        Assistant_Manager = "AM","Boshqaruvchi yordamchisi"
        Designer = "DE","Dizayner"
        Welder = "WD","Payvandchi"
        Accountant = "AC","Buxgalter"
        Storekeeper = "SK","Do'kondor"
        Secretary = "SC","Secretary"
        Loader = "LD","Yuklovchi"
        Electrician = "EL","Elektrchi"
        Cook = "CO","Oshpaz"
        Economist ='EC','Iqtisodchi'
        Merchandiser = 'ME','Merchandiser'
        System_Administrator = 'SA','Tizim Administratori'
        Tourist = 'TO','Turist'

    class Ru_Status(models.TextChoices):
            Courier = 'CR','Курьер'
            Driver  = 'DV','Водитель'
            Salesman = "SM",'Продавец'	
            Cashier = "CI",'Кассир'
            Administrator = "AD","Администратор"
            Operator = "OR",'Оператор'
            Programmer = "PR",'Программист'
            Manager = "MR" ,'Менеджер'
            Assistant = "AS",'Помощник'
            Builder = "BU",'Строитель'
            Assistant_Manager = "AM",'Помощник управляющего'
            Welder = "WD",'Сварщик'
            Accountant = "AC",'Бухгалтер'
            Engineer = "EG",'Инженер'
            Director = "DR",'Директор'
            Storekeeper = "SK",'Кладовщик'
            Secretary = "SC",'Секретарь'
            Lawyer = "LW","Юрист"
            Loader = "LD","Грузчик"
            Cleaner = "CL",'Уборщик'
            Designer = "DE",'Дизайнер'
            Electrician = "EL",'Электрик'
            Cook = "CO",'Повар'
            Economist ='EC','Экономист'
            Merchandiser = "MD",'Мерчендайзер'
            System_Administrator = "SA",'Системный Администратор'
            Waiter = 'WA','Официант'
            Supervisor = 'SU','Супервайзер'
 