from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fruit
from .forms import FruitForm


"""
View will take in a repsonse as a param and return either a httpresponse or render a template
"""
# Create your views here.
def produceSector(request): 
    return render(request, 'firstApp/home.html')  

# Create your views here.
def marketSector(request):
    fruits =  Fruit.objects.all()
    context = {"fruits":fruits} 
    return render(request, 'firstApp/market.html', context)  


"""
Create Read Update Delete (CRUD) OPERATIONS: 

"""

def createFruit(request):
    form = FruitForm()
    context = {"form":form}

    if request.method == "POST":
        form = FruitForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("market")            

    return render(request, "firstApp/form.html", context )

def readAllFruits(request):
    fruits = Fruit.objects.all() # ORM helps us not write sQL syntax here => transalates to SELECT * FROM fruits;
    context = {"fruits":fruits}
    return render(request,"firstApp/market.html", context)

def readOneFruit(request,pk):
    fruit = Fruit.objects.get(id = pk)
    context ={"fruit":fruit}
    return render(request,"firstApp/fruit_details.html", context)

def updateFruit(request):
    return render(request)

def deleteFruit(request):
    return render(request)