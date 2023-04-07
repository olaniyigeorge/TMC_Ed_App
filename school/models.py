from django.db import models

# Create your models here.
class User(models.Model):
    surname = models.CharField(max_length=16)
    firstname = models.CharField(max_length=16)
    lastname = models.CharField(max_length=16)
    email = models.EmailField()

class Student(User):
    
    registered_subjects = []

    def __str__(self):
        return f"{self.surname} {self.firstname}"

class Staff(User):

    level = models.IntegerField()
    is_administrative = models.BooleanField()
    is_teacher = models.BooleanField()

    subjects_taught = []

    def __str__(self):
        return f"{self.surname} {self.firstname}"

class Class(models.Model):
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [(JUNIOR, 'Junior'), (SENIOR, 'Senior')]
    
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default=JUNIOR)
    level = models.IntegerField()

    def __str__(self):
        return f"{self.year_in_school}{self.level}"
