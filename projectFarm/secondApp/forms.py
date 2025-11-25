from django.forms import ModelForm
from .models import Vegetable, Flower

class VegetableForm(ModelForm):
    class Meta: 
        model = Vegetable
        fields = '__all__'
    
class FlowerForm(ModelForm):
    class Meta:
        model = Flower
        fields = '__all__'