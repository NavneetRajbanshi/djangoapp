from travels.models import Destination
from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Abu Dhabi'
    dest1.desc = 'The forgotten kingdom'
    dest1.img = 'dubai.jpg'
    dest1.price = 650

    dest2 = Destination()
    dest2.name = 'Thailand'
    dest2.desc = 'The forgotten kingdom'
    dest2.img = 'thailand.jpg'
    dest2.price = 845

    dest3 = Destination()
    dest3.name = 'France'
    dest3.desc = 'The forgotten kingdom'
    dest3.img = 'france.jpg'
    dest3.price = 450

    
    dest4 = Destination()
    dest4.name = 'Switzerland'
    dest4.desc = 'The forgotten kingdom'
    dest4.img = 'switzerland.jpg'
    dest4.price = 1030

    dest5 = Destination()
    dest5.name = 'Italy'
    dest5.desc = 'The forgotten kingdom'
    dest5.img = 'italy.jpg'
    dest5.price = 650

    dest6 = Destination()
    dest6.name = 'England'
    dest6.desc = 'The forgotten kingdom'
    dest6.img = 'england.jpg'
    dest6.price = 950

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    
    return render(request,'travels/index.html', {'dests' : dests })