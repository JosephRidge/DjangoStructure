from django.forms import ModelForm
from .models import Fruit

class FruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__' # or target specific columns eg ['name', 'description', 'price]
