from django.contrib import admin
from django.urls import path

urlpatterns = [
            path('admin/', admin.site.urls),
            path('',views.index,name='index'),
            path('home/',views.home,name='home'),
            path('aboutus/',views.aboutus,name='aboutus'),
            path('myhobbies/',views.myhobbies,name='myhobbies'),
        ]
