from django.urls import path
from . import views

app_name = 'membership'

urlpatterns = [
    path('', views.MembershipList.as_view(), name='membershiplist'),
]
