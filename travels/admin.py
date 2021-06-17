from django.contrib import admin
from .models import Destination, Traveler, Contact

# Register your models here. 

admin.site.register(Destination)
admin.site.register(Traveler)
admin.site.register(Contact)