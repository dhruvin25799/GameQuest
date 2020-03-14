from django.urls import path
from . import views

app_name='package'

urlpatterns = [
    path('',views.PackageList.as_view(),name='packagelist'),
]
