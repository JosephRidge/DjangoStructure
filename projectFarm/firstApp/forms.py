from django.forms import ModelForm # helps use create the input form
from .models import Fruit # helps us bring in the data structure

class FruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__' # or target specific columns eg ['name', 'description', 'price]
