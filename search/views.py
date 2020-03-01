from django.shortcuts import render
from products.models import Perfume

# Create your views here.
def do_search(request):
    perfumes = Perfume.objects.filter(name__icontains=request.GET['do_search'])
    return render(request, "index.html", {"perfumes":perfumes})

def do_search_F(request):
    perfumes = Perfume.objects.filter(gender= 'F')
    return render(request, 'index.html', {'perfumes': perfumes})
def do_search_M(request):
    perfumes = Perfume.objects.filter(gender= 'M')
    return render(request, 'index.html', {'perfumes': perfumes})
def do_search_U(request):
    perfumes = Perfume.objects.filter(gender= 'U')
    return render(request, 'index.html', {'perfumes': perfumes})  