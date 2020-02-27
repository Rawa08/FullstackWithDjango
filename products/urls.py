
from django.conf.urls import url
from .views import post_detail


urlpatterns = [
    url(r'^$', post_detail, name='product'),
    
]