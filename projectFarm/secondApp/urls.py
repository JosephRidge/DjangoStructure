from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home,name='home'),
    # CRUD OPERATIONS ON VEGETABLE model
    path('create', views.createVegetable, name='create'),
    path('vegetables', views.fetchAllVegetables, name='fetchAll'),

    path('create-flower', views.createFlower, name='create-flower'),
    path('read-flowers', views.readFlowers, name='read-flowers'),
    path('read-flowers/<str:pk>', views.readOneFlower, name='read-one-flower'),
    path('update-flower/<str:pk>', views.updateFlower, name='update-flower'),
    path('delete/<str:pk>', views.updateFlower, name='delete-flower'),
    path('prompt-delete/<str:pk>', views.promptDelete, name='prompt-delete-flower')

]