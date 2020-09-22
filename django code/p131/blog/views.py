from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator


# Create your views here.
def post_list(request):
    all_post = Post.objects.all()
    paginator = Paginator(all_post, 4, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'page_obj': page_obj})
