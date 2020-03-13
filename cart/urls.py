
from django.conf.urls import url
from .views import my_cart, add_product, adjust, delete_from_cart


urlpatterns = [
    url(r'^$', my_cart, name='my_cart'),
    url(r'^add/(?P<id>\d+)', add_product, name='add_product'),
    url(r'^adjust/(?P<id>\d+)', adjust, name='adjust'),
    url(r'^delete/(?P<id>\d+)', delete_from_cart, name='delete'),
]