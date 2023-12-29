from django.db import models

# Create your models here.

class titanic(models.Model):
    PASSENGER_CLASS_CHOICES = (('First_Class','1'),
                               ('Second_Class','2'),
                               ('Third_Class','3'))
    
    STARTING_POINT_CHOICES = (('S','0'),('C','1'),('Q','2'))

    SIBLINGS_SPOUSE_CHOICES = (('Siblings_Spouse','1'),
                               ('No Siblings_Spouse','0'))
    
    PARENTS_CHILDREN_CHOICES = (('Parents_Children','1'),
                        ('No_Parents_Children','0'))
    

    GENDER_CHOICES = (('Male', '0'),
                    ('Female','1'))
    
    Age = models.CharField(max_length=5)
    Passenger_Class = models.CharField(max_length=30,choices=PASSENGER_CLASS_CHOICES)
    Starting_Point = models.CharField(max_length=15, choices= STARTING_POINT_CHOICES)
    Siblings_Spouse = models.CharField(max_length=30,choices=SIBLINGS_SPOUSE_CHOICES)
    Parents_Children = models.CharField(max_length=30,choices=PARENTS_CHILDREN_CHOICES)
    Gender = models.CharField(max_length=15, choices=GENDER_CHOICES)



  
