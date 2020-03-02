from django.conf.urls import url
from .views import  logout, login, user_registration



urlpatterns =[
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', user_registration, name="register"),
    
]