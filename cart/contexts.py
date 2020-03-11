from django.shortcuts import get_object_or_404
from products.models import Perfume


def cart_content(request):
    """
    retriving cart item from session, make it avilable to render on other pages
    """
  
    cart = request.session.get('cart', {})

    cart_item = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Perfume, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_item.append({'id': id, 'quantity': quantity, 'product': product})
    
    return {'cart_item': cart_item, 'total': total, 'product_count': product_count}

def select_qty(request):
  #let user to choose up to 999 pices of a product"""
    select_qty_999 = range(0,1000)
#let user to choose up to 5 pices of a product"""
    select_qty_5 = range(1, 6)
    return {'select_qty_999':select_qty_999, 'select_qty_5':select_qty_5}