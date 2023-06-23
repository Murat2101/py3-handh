from django.shortcuts import render
from  .models import *
# Create your views here.

def workers(request):
    workers = Worker.objects.all()
    context = {"workers": workers}
    return render(request, 'workers.html')
