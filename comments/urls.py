from django.conf.urls import url
from. views import post_detail


urlpatterns =[
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
   

]
