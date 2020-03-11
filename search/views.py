from django.shortcuts import render
from products.models import Perfume
from django.contrib.postgres.search import SearchVector

# Create your views here.
def do_search(request):
    """seraching for word provided by user in name, brand decription and gender
    """
    perfumes =Perfume.objects.annotate(search=SearchVector('name', 'brand', 'description', 'gender'),).filter(search__icontains=request.GET['do_search'])
    return render(request, "index.html", {"perfumes":perfumes})




# Rendering products for the selected gender by user

def do_search_F(request):
    
    perfumes = Perfume.objects.filter(gender= 'female')
    return render(request, 'index.html', {'perfumes': perfumes})
def do_search_M(request):
    perfumes = Perfume.objects.filter(gender= 'male')
    return render(request, 'index.html', {'perfumes': perfumes})
def do_search_U(request):
    perfumes = Perfume.objects.filter(gender= 'unisex')
    return render(request, 'index.html', {'perfumes': perfumes})  