from django.urls import path # helps us import the method path for our endpoints
from . import views # import veiws from the current root directory

# endpoints + target view functions
urlpatterns = [
    path('', views.produceSector, name ='home'),
    path('produce', views.produceSector, name ='produce'),
    path('market', views.marketSector, name ='market'),
    # FRUITS CRUD Operations
    path('create', views.createFruit, name ='create'),
    path('readAll', views.marketSector, name ='readAll'),
    path('readOne/<str:pk>', views.readOneFruit, name ='readOne'),
    path('update', views.marketSector, name ='update'),
    path('delete', views.marketSector, name ='delete'),
]