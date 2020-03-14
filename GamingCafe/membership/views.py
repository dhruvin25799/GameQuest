from django.shortcuts import render
from django.views import generic
from .models import Membership
# Create your views here.


class MembershipList(generic.ListView):
    model = Membership
    template_name = 'membership_list.html'
