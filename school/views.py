from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class SchoolPage(TemplateView):
    template_name='school.html'