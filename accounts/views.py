from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm
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
    if request.user.is_authenticated:
        return redirect(reverse('home_page'))

  #login User and return login page
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