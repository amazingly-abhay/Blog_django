#this url module is similar to the url module pre defined in <project name==mysite(here)> directory

from django.urls import path  # type: ignore
from.import views                   #importing views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('about/', views.about, name="about-page"),
    
]


