from django.shortcuts import render, redirect, reverse

# Create your views here.

def my_cart(request):
    return render(request, 'cart.html')


def add_product(request, id):
    quantity = int(request.POST.get('quantity')) 

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('home_page'))





def adjust(request, id):
   
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('my_cart'))    