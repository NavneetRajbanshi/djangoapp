from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'name': ''}
    return render(request,'travels/index.html', context)