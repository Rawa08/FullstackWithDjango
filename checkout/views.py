import os
from django.shortcuts import render,  get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerPaymentForm, CustomerShippingForm
import stripe
from django.utils import timezone
from django.contrib import messages
from products.models import Perfume
from .models import OrderLineItem
# Create your views here.

stripe.api_key = os.environ.get("StripeApiKey")


@login_required
def checkout(request):
    if request.method == 'POST':
        customer = CustomerShippingForm(request.POST)
        payment = CustomerPaymentForm(request.POST)
        if customer.is_valid() and payment.is_valid():
            order = customer.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Perfume, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(amount=int(
                    total * 100), currency="EUR", description=request.user.email, card=CustomerPaymentForm.cleaned_data['stripe_id'])
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('home_page'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(CustomerPaymentForm.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment = CustomerPaymentForm()
        customer = CustomerShippingForm()
    
    return render(request, "checkout.html", {"customer": customer, "payment": payment, "publishable": os.environ.get("publishable")})