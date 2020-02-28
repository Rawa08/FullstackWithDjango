from .models import Perfume
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from products.models import Perfume


# Create your views here.

def post_detail(request, slug):
    perfumes = Perfume.objects.all()
    template_name = 'products.html'
    product = get_object_or_404(Perfume, slug=slug)
    comments = product.review.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, 
    {'product': product,'comments': comments,'new_comment': new_comment,'comment_form': comment_form,'perfumes': perfumes})









