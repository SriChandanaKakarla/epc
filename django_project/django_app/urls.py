from django.urls import path
from . import views

urlpatterns = [
path('',views.home, name = 'home'),
    path('login/',views.login, name = 'login'),

path('register',views.register,name='register'),
path('home',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
path('seeall',views.seeall,name='seeall'),
    path('show',views.show,name='show'),
    path('pro',views.pro,name='pro'),
path("send_otp",views.send_otp,name="send otp"),
    path("otp",views.otp,name="otp"),
]
