from travels.models import Destination
from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Mustang'
    dest1.desc = 'The forgotten kingdom'
    dest1.price = 1400

    dest2 = Destination()
    dest2.name = 'Mustang'
    dest2.desc = 'The forgotten kingdom'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650

    dest3 = Destination()
    dest3.name = 'Mustang'
    dest3.desc = 'The forgotten kingdom'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750

    
    dest4 = Destination()
    dest4.name = 'MMustang'
    dest4.desc = 'The forgotten kingdom'
    dest4.price = 1400

    dest5 = Destination()
    dest5.name = 'Mustang'
    dest5.desc = 'The forgotten kingdom'
    dest5.img = 'destination_2.jpg'
    dest5.price = 650

    dest6 = Destination()
    dest6.name = 'Mustang'
    dest6.desc = 'The forgotten kingdom'
    dest6.img = 'destination_3.jpg'
    dest6.price = 750

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    
    return render(request,'travels/index.html', {'dests' : dests })