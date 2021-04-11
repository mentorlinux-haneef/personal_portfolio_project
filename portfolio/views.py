from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    pobj = Project.objects.all()
    return render(request, 'portfolio/home.html', {'pobj':pobj})