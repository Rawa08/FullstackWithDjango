
from django.conf.urls import url
from .views import get_contact_page, send_email


urlpatterns = [
    url(r'^$', get_contact_page, name='contact_page'),
    url(r'^send/', send_email, name='send_email'),
    
    
]