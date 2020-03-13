from django.shortcuts import render, redirect, reverse

# Create your views here.


def my_cart(request):
    """
    render cart page
    """
    cart_template = 'cart.html'

    return render(request, cart_template)


def add_product(request, id):

    # Add a quantity of a specified product to the cart in session

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('home_page'))


def adjust(request, id):

    # Adjust the quantity of the specified product to the specified amount

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('my_cart'))


def delete_from_cart(request, id):

    # Remove item from cart

    quantity = int(0)
    cart = request.session.get('cart', {})
    cart[id] = quantity
    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('my_cart'))
