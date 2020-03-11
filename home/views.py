from django.shortcuts import render
from products.models import Perfume


# Create your views here.
def home_page(request):
    """
    Render the home page and retrive the products in db
    """
   
    perfumes = Perfume.objects.all()
     
    return render(request, 'index.html', {'perfumes': perfumes})

      

       
   