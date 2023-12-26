from django.urls import path , include
from . import views

urlpatterns = [

    path('',views.index,name = ' Myrestudent'),
    path ('about/',views.about,name = 'about'),
    path ('home/',views.home,name = 'home'),
    path ('show/',views.show,name = 'show')
]