from django.conf.urls import url
from django.contrib import admin
from main import views
from django.urls import path


app_name ='main'

urlpatterns = [
    url(r'^home/',views.index,name='index'),
    url(r'^formpage/',views.formNew,name='formNew' ),
]
