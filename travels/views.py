from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'name': 'static'}
    return render(request,'travels/index.html', context)