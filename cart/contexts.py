from django.shortcuts import get_object_or_404
from products.models import Perfume


def cart_content(request):
  
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