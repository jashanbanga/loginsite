from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
path('',views.usersearch),
path('repo/<reponame>',views.repos,name='reponame'),
]
