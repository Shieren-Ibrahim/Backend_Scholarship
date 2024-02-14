
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('login',views.login,name='login'),
    path('forgetten_password',views.forgetten_password,name='forgetten_password'),
    path('signup',views.signup,name='signup'),
    path('confirm',views.confirm,name='confirm'),
    path('get_sholarships',views.get_sholarships,name='get_sholarships'),
    path('set_rating',views.set_rating,name='set_rating'),
    path('get_specialization',views.get_specialization,name='get_specialization'),
    path('get_stage',views.get_stage,name='get_stage'),
    path('get_SchlarshipForCountry',views.get_SchlarshipForCountry,name='get_SchlarshipForCountry'),
    path('get_SchlarshipForUniversity',views.get_SchlarshipForUniversity,name='get_SchlarshipForUniversity'),
    path('get_free',views.get_free,name='get_free'),
    path('get_university',views.get_university,name='get_university'),
    path('submit_request',views.submit_request,name='submit_request'),
    path('get_orderAndNotification',views.get_orderAndNotification,name='get_orderAndNotification'),
    path('cancel_order',views.cancel_order,name='cancel_order'),
    path('getOrder',views.getOrder,name='getOrder'),
    path('UpdateOrder',views.UpdateOrder,name='UpdateOrder'),
    path('UpdateProfile',views.UpdateProfile,name='UpdateProfile'),
    path('contact_us',views.contact_us,name='contact_us'),
    
    
]
