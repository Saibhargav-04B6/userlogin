from django.shortcuts import render,redirect
from django.core.cache import cache
from .forms import ProductForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# @login_required
def home(request):
    data=cache.get('mydata')
    if not data:
        data='mydetails'
        cache.set('mydata',data,timeout=3600)
    return render(request,'home.html')
def authview(request):
    form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})
def createproduct(request):
    if(request.method=='POST'):
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form=ProductForm()
    return render(request,'createproduct.html',{'form':form})