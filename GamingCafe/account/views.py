from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from . import forms
from .models import UserProfile,User,Receipt
from package.models import Package
# Create your views here.


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


class MyProfile(generic.DetailView):
    template_name = 'my_profile.html'
    model = UserProfile
    context_object_name = 'userprofile'

    def get_object(self, queryset=None):
        username = self.kwargs['username']
        user = User.objects.get(username=username)
        userprofile = UserProfile.objects.get(user=user)
        return userprofile


class ConfirmBuyPackage(generic.TemplateView):
    template_name='confirmbuypackage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_user = UserProfile.objects.get(user=self.request.user)
        context["curr_user"] = curr_user
        package = Package.objects.get(pk=self.kwargs.get('package_pk'))
        context["package"] = package
        total_discount = package.price * \
            (curr_user.membership_status.discount_offered/100)
        context["total_discount"]=total_discount
        context["total_amount"] = package.price-total_discount
        return context
    

class PackageBuy(generic.TemplateView):
    template_name='buypackage.html'
    def get(self, request, *args, **kwargs):
        user = self.request.user
        userprofile = UserProfile.objects.get(user=user)
        package = Package.objects.get(pk=self.kwargs.get('package_pk'))
        membership = userprofile.membership_status
        discount = membership.discount_offered
        price = package.price
        discount_amt = price*(discount/100)
        total = price - discount_amt
        receipt = Receipt(user=userprofile, package=package, purchase_date=timezone.now(
        ), mrp=package.price, discount=discount, amount=total)
        receipt.save()
        return super().get(request, *args, **kwargs)
