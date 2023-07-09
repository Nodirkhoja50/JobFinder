from django.db import models

# Create your models here.
class Specialty(models.Model):
    class Status(models.TextChoices):
        Courier = "CR","Courier"
        Driver  = "DR","Driver"
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
        Merchandiser = 'MR','Merchandiser'
        System_Administrator = 'SA','System_Administrator'
        Waiter = 'WA','Waiter'
        Supervisor = 'SU','Supervisor'