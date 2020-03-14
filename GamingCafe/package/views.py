from django.shortcuts import render
from django.views import generic
from .models import Package
# Create your views here.


class PackageList(generic.ListView):
    model = Package
    template_name='plans.html'
