from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
path('',views.reposearch),
path('repo/<reponame>',views.commithist,name='reponame'),
]
