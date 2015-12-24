from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class College(models.Model):
    #name of the college from the dropdown list generated from csv file
    name = models.CharField('name', max_length=500)
    location = models.CharField('address', max_length=100)
    university = models.CharField('University1', max_length=500)

    def get_name(self):
    	return self.name

    def get_location(self):
    	return self.location

    def get_university(self):
    	return self.university

class Employee(models.Model):    
    employee = models.CharField(max_length=200)
    emplocation = models.CharField(max_length=200)

    def get_employee(self):
    	return self.employee

    def get_emplocation(self):
    	return self.emplocation

class IncomeBoost(models.Model):
    annualsalary = models.DecimalField(max_digits=12, decimal_places=2)
    dependents = models.DecimalField(max_digits=2, decimal_places=0)
    kids = models.DecimalField(max_digits=1, decimal_places=0)
    certification = models.CharField("certification_name", max_length=500)
    
    def get_annualsalary(self):
    	return self.annualsalary

    def get_dependents(self):
    	return self.dependents

    def get_kids(self):
    	return self.kids

    def get_certification(self):
    	return self.certification

class CourseRank(models.Model):
    courses = models.CharField("course_name", max_length=100)

    def get_courses(self):
        return self.courses

    #define the methods here
 #   def get_id(self):
 #   	return self.id

    

    

    





    
        
    

