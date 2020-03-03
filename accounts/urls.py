from django.conf.urls import url, include
from .views import  logout, login, user_registration
from accounts import url_reset



urlpatterns =[
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', user_registration, name="register"),
    url(r'^password-reset/', include(url_reset)),
    
]