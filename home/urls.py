from django.conf.urls import url
from .views import home_page, do_search



urlpatterns =[
    
    url(r'^$', do_search, name="do_search")
]