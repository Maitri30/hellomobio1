from django.shortcuts import render,redirect
from .forms import CategoriesForm, ProductForm
from .models import Categories

# Create your views here.



def welcome(request):
    return render(request, "welcome.html")

def load_form(request):
    form = CategoriesForm
    return render(request, "index.html",{'form':form})

def add(request):
    form = CategoriesForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    categories = Categories.objects.all
    return render(request, 'show.html',{'categories':categories})


def edit(request, id):
    categories = Categories.objects.get(id=id)
    return render(request, 'edit.html',{'categories':categories})

def update(request, id):
    categories = Categories.objects.get(id=id)
    form = CategoriesForm(request.POST, instance=categories)
    form.save()
    return redirect('/show')
    
def delete(request, id):
    categories = Categories.objects.get(id=id)
    categories.delete()
    return redirect('/show')

def addproduct(request):
    form = ProductForm
    return render(request, 'product.html',{'form':form})

def padd(request):
    form = ProductForm(request.POST)
    form.save()
    return redirect('/show')