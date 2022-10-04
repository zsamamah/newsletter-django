from django.shortcuts import render
from app1.models import Post


# Create your views here.
def home(request):
    temp = 'zaido'
    title = 'Home'
    context = {'posts': Post.objects.all(), 'temp': temp, 'title': title}
    return render(request, 'app1/index.html', context)


def about(request):
    title = 'About Us'
    return render(request, 'app1/about.html', {'title': title})


def contacts(request):
    title = 'Contact Us'
    return render(request, 'app1/contact.html', {'title': title})
