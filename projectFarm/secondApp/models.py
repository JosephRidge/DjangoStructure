from django.db import models

# Create your models here.
class Vegetable(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    health_benefits =  models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Name: {self.name}. Price: {self.price}" 


class Flower(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    color =  models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now=True)

    # TODO: Figure out!
    # class Meta:
    #     ordering = ["-created_at"]

    def __str__(self):
        return f"Name: {self.name}. Price: {self.price}" 


