from django.shortcuts import render

# Create your views here.
def travel_list(request):
    return render(request, 'travels/travel_list.html')