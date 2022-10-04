from django.shortcuts import render
from django.contrib import messages
from user.forms import UserRegForm

# Create your views here.

def home_user(request):
    return render(request, 'user/index.html')

def register(request):
    if request.method=='POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            fname = form.cleaned_data.get('first_name')
            form.full_clean()
            messages.success(request,'Account created for {} @$ {} !'.format(fname,username))
            # return redirect('home_page')
            
    else:
        form = UserRegForm()
    return render(request,'user/register.html', {'form':form})
