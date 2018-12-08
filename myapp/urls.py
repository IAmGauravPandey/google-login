from django.urls import path
from . import views
from django.conf.urls import url,include
from django.contrib import admin,auth


urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]