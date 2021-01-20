from django.shortcuts import render, redirect
from .forms import productsForm
from .models import products

# Create your views here.


def product_list(request):
    context = {'product_list': products.objects.all()}
    return render(request, "projectapp/list.html", context)


def product_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = productsForm()
        else:
            product = products.objects.get(pk=id)
            form = productsForm(instance=product)
        return render(request, "projectapp/form.html", {'form': form})
    else:
        if id == 0:
            form = productsForm(request.POST)
        else:
            product = products.objects.get(pk=id)
            form = productsForm(request.POST,instance= product)
        if form.is_valid():
            form.save()
        return redirect('/list')
