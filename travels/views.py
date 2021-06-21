from os import name
from django.core.checks import messages
import travels
from travels.models import Destination
from django.shortcuts import render
from .models import Destination, Traveler, Contact
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def index(request):

    form = ContactForm()
    if request.method == 'POST':
        print(request.POST)
    context = {'form' :form}
    dests = Destination.objects.all()
    travelers = Traveler.objects.all()
    

    return render(request,'travels/index.html', {'dests': dests, 'travelers': travelers, 'context': context})
