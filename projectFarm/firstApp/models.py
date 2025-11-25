from django.db import models

# Create your models here.
class Produce(models.Model): # name of the table 
    name = models.CharField(max_length=200) # strings with a max length in character of 200
    description = models.CharField(max_length=255) # strings with a max length in character of 255
    price = models.FloatField() # float numbers eg 20.25

    def __str__(self):
        return self.name
 
class Fruit(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255) # strings with a max length in character of 255
    price = models.FloatField() # float numbers eg 20.25
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # class Meta: 
    #     ordering = [-created_at,-updated_at]

    def __str__(self):
        return self.name