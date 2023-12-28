from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Items, Colors, Size, Category
from .forms import Itemsform

# Create your views here.

def InventoriesIndex(request):
    tms = Items.objects.all()
    return render(request, "Inventories/inventoriesIndex.html", {"items":tms})

def newInventories(request):
    IF = Itemsform(request.POST)
    
    if IF.is_valid():
        IFsav = IF.save()
        col = IF.cleaned_data.get('color')
        siz = IF.cleaned_data.get('size')
        cat = IF.cleaned_data.get('category')
        if col == Colors.objects.get(name = "New Color"):
            newCol = request.POST.get('NewColor')
            Colors.objects.create(name = newCol)
            IFsav.color = Colors.objects.get(name = newCol)
            IFsav.save()
            # return HttpResponse(Colors.objects.create(name = newCol))
        if siz == Size.objects.get(name = "New Size"):
            newSiz = request.POST.get('NewSize')
            Size.objects.create(name = newSiz)
            IFsav.size = Size.objects.get(name = newSiz)
            IFsav.save()
        if cat == Category.objects.get(name = "New Category"):
            newCat = request.POST.get('NewCategory')
            Category.objects.create(name = newCat)
            IFsav.category = Category.objects.get(name = newCat)
            IFsav.save()
        return redirect('/invent')
    else:
        IF = Itemsform(request.POST)
    return render(request, "Inventories/generate.html", {"Itemsform":IF})

def viewInvent(request, id):
    tms = Items.objects.get(id = id)
    return render(request, "Inventories/view.html", {"items":tms})

def editInvent(request, id):
    tms = Items.objects.get(id = id)
    IF = Itemsform(request.POST)
    if IF.is_valid():
        tms.admin_name = IF.cleaned_data.get('admin_name')
        tms.quantity = IF.cleaned_data.get('quantity')
        tms.color = IF.cleaned_data.get('color')
        tms.size = IF.cleaned_data.get('size')
        tms.category = IF.cleaned_data.get('category')
        tms.update_Date = IF.cleaned_data.get('update_Date')
        tms.save()
        return redirect('/invent')
    else:
        IF = Itemsform(request.POST)
    return render(request, "Inventories/edit.html", {"Itemsform":IF})