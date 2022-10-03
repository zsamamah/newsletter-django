from django.shortcuts import render
from app1.models import Post


# Create your views here.
def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
