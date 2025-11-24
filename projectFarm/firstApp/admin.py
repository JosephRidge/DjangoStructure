from django.contrib import admin
from . import models # models

# Register your models here.
admin.site.register(models.Produce)
admin.site.register(models.Fruit)