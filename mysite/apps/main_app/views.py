# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'main_app/index.html' )

def experience(request):
	return render(request, 'main_app/experience.html')

def projects(request):
	return render(request, 'main_app/projects.html')

def blog(request):
	return render(request, 'main_app/blog.html')

# the views past this point are linked to from the projects.html page
