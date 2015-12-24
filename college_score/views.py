from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.core import serializers
import os,re,math
import json
from django import forms

# Create your views here.

def change_attributes(annualsalary, certi_salary):
	return float(annualsalary) / 12
	return float(certi_salary) / 12




def income_boost(certi_salary, annualsalary):
	base = 0.35
	kid = 0.04 * kids
	dependent = 0.02 * dependents
	total_expense = float(base + kids + dependent) * float(annualsalary)
	disposable_sal = float(annualsalary) - float(total_expense)
    post_avg = float(certi_salary)
    increment = float(annualsalary) - float(avg_sal_post)
    boost = .50 * increment
    revised_disposable = float(disposable_sal) + float(boost)
    percent_increase = (float(revised_disposable)- float(disposable_sal) / revised_disposable) * 100
    return percent_increase
    if (percent_increase >= 50):
    	print "Income boost score is 10"
    
    if (percent_increase < 50 & percent_increase > 40) :
    	print "Income boost score is 8"

    elif:
    	(percent_increase < 40 & percent_increase > 30) :
    	print "Income boost score is 5"

    elif:
    	(percent_increase < 30 & percent_increase > 20) :
    	print "Income boost score is 3"

    else:
    	print "Sorry your income boost is very low 0"

def uni_score(name):
	


def course_score(course_name):



class MyForm(forms.Form) :
	'''Class with a form with the attributes '''
	name = forms.CharField(max_length=500)
	location = forms.CharField(max_length=100)
	university = forms.CharField(max_length=500)
	employee = models.CharField(max_length=200)
    emplocation = models.CharField(max_length=200)
    annualsalary = models.DecimalField(max_digits=12, decimal_places=2)
    dependents = models.DecimalField(max_digits=2, decimal_places=0)
    kids = models.DecimalField(max_digits=1, decimal_places=0)
    courses = models.CharField("course_name", max_length=100)
    certification = models.CharField("certification_name", max_length=500)

def formview(request):
	'''A view for the main form in which user enters the information required'''
	#if the form has been submitted
	if request.method == 'POST':
		#A form boud to the POST data that has fields for user name and user password
		form = MyForm(request.POST)

		#After valudation of user information
		if form.is_valid():			
			#annual salary of the borrower
			annualsalary = form.cleaned_data['annualsalary']
            
            #certification of the user
            certification = form.cleaned_data['certification']

			#check that names exist in the database
			
			if (College.objects.filter(certification_name=certification).exits() and College.objects.filter(name = name).exits()):
			    mysal = College.objects.get(certification_name=certification).get.salary()
			    certi_salary = float(mysal) / 12
			    myincomeboost = income_boost(certi_salary)

			    #render out.html, page telling the user the distance
			    return render(request, 'college_score/out.html', {'income_boost' : myincomeboost})

			else:

				#Redirect to fail page
				return HttpResponseRedirect('college_score/fail')





