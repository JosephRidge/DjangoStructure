from django.urls import path # helps us import the method path for our endpoints
from . import views # import veiws from the current root directory

# endpoints + target view functions
urlpatterns = [
    path('produce', views.produceSector)
]