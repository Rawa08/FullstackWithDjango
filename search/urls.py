from django.conf.urls import url
from .views import  do_search, do_search_F, do_search_M, do_search_U



urlpatterns =[
    url(r'^$', do_search, name="do_search"),
    url(r'^F/$', do_search_F, name="do_search_F"),
    url(r'^M/$', do_search_M, name="do_search_M"),
    url(r'^U/$', do_search_U, name="do_search_U"),
    
  
    
]