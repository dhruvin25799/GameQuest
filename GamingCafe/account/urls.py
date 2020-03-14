from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my_profile/<username>', views.MyProfile.as_view(), name='profile'),
    path('buy/confirm_buy/<package_pk>/<curr_user>',views.ConfirmBuyPackage.as_view(), name='confirmbuypackage'),
    path('buy/success/<package_pk>/<curr_user>',views.PackageBuy.as_view(),name='buypackagesuccess'),
]
