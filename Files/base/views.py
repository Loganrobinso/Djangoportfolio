from django.shortcuts import render


# This python file render our templates
# Create your views here.
def home(request):
    return render(request, 'base/home.html')
