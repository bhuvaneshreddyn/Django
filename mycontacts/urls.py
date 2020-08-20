from django.urls import path
from django.conf.urls import url, include
from mycontacts import views

urlpatterns=[
            url('whoami.*',views.name,name='name'),
            #url('phonenumber.*',views.phonenumber,name='phonenumber'),
            url('',views.index,name='index')
            ]
