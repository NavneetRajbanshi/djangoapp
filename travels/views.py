from os import name
from django.core.checks import messages
import travels
from travels.models import Destination
from django.shortcuts import render
from .models import Destination, Traveler
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def index(request):
    
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Thank you for your interaction")

    context = {'form': form}
    dests = Destination.objects.all()
    travelers = Traveler.objects.all() 
    

    return render(request,'travels/index.html', {'dests': dests, 'travelers': travelers, 'context': context})

