from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def logout(request):
    """Log out the User
    """
    auth.logout(request)
    messages.success(request, 'You have successfully been logged out!')
    return redirect(reverse('home_page'))

def login(request):
    """
    Log in User and redirect to the home page
    """
    if request.user.is_authenticated:
        return redirect(reverse('home_page'))

 
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['Username'],
                                    password=request.POST['password'])
            

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('home_page'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def user_registration(request):
    """
    Registration of a new user
    """
    
    if request.user.is_authenticated:
        return redirect(reverse('home_page'))

    if request.method=='POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
            password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request,'You have successfully registered')
                return redirect(reverse('home_page'))
                
            else:
                messages.error(request, 'unable to register')    
    else:
        registration_form=UserRegistrationForm()
    return render(request, 'registration.html', {'registration_form':registration_form})