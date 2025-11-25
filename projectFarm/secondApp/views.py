from django.shortcuts import render, redirect
from .forms import VegetableForm, FlowerForm
from .models import Vegetable, Flower

# Create your views here.
def home(request):
    return render(request, "secondApp/home.html")

def createVegetable(request):
    form = VegetableForm()

    if request.method =="POST":
        form = VegetableForm(request.POST) # retreives the user input
        if form.is_valid(): #
            form.save()
            return redirect("fetchAll")

    context = {"form":form}
    return render(request, "secondApp/form.html", context)

def fetchAllVegetables(request):
    vegetables = Vegetable.objects.all()
    context = {"vegetables": vegetables}
    return render(request,"secondApp/home.html" ,  context)



# CREATE FLOWER

def createFlower(request):
    form = FlowerForm()
    #  retreiving user input
    if request.method == "POST":
        form = FlowerForm(request.POST) # gets user input
        if form.is_valid():
            form.save() # saves to DB
            return redirect("read-flowers")
    context = {"form":form}
    return render(request, "secondApp/form.html", context)

def readFlowers(request):
    flowers = Flower.objects.all() # fetches all the flower data
    context = {"flowers":flowers}
    return render(request, "secondApp/flowers.html",context)

def readOneFlower(request, pk):
    flower = Flower.objects.get(id=pk)
    context = {"flower":flower}
    return render(request, "secondApp/flower.html",context)

def updateFlower(request, pk):
    flower = Flower.objects.get(id = pk) # fetch the data
    form = FlowerForm(instance = flower) # get the inital flower details

    if request.method == "POST":
        form = FlowerForm(request.POST, instance = flower)
        if form.is_valid():
            form.save()
            return redirect("read-flowers")

    context = {"form":form}
    return render(request, "secondApp/form.html", context)

def promptDelete(request, pk):
    flower = Flower.objects.get(id=pk)
    context = {"flower":flower}
    return render(request, "secondApp/prompt_delete.html", context)

def deleteFlower(request, pk):
    flower = Flower.objects.get(id=pk)
    if flower:
        Flower.objects.delete(id=pk)
        return redirect("read-flowers")
    context = {"flower":flower}
    return render(request,"secondApp/delete.html", context)
