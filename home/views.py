from django.shortcuts import render, redirect, reverse
from products.models import Perfume



# Create your views here.
def home_page(request):
   
    perfumes = Perfume.objects.all()
     #perfumes = Perfume.objects.filter(gender= 'M')
    return render(request, 'index.html', {'perfumes': perfumes})





def do_search(request):
    perfumes = Perfume.objects.filter(name__icontains=request.GET['do_search'])
    return render(request, "index.html", {"perfumes":perfumes})
    