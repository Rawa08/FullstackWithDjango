from django.shortcuts import render,redirect, reverse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import os



# Create your views here.
def get_contact_page(request):

    return render(request, 'contact.html')
   
    


def send_email(request):
    subject = request.POST.get('name')
    message = request.POST.get('text')
    from_email = request.POST.get('from_email')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [os.environ.get('admin_mail')])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'contact_success.html')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.') 



       