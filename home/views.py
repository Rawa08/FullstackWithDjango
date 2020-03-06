from django.shortcuts import render
from products.models import Perfume


# Create your views here.
def home_page(request):
   
    perfumes = Perfume.objects.all()
     #perfumes = Perfume.objects.filter(gender= 'M')
    return render(request, 'index.html', {'perfumes': perfumes})

      

       
   