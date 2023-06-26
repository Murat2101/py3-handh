from django.shortcuts import render
from .models import *
from core.models import *
# Create your views here.

def workers(request):
    workers = Worker.objects.all()
    context = {"workers": workers}
    return render(request, 'workers.html')

def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    # SELECT * FROM Worker WHERE id={id}
    context = {'worker': worker_object}
    return render(request, 'worker.html', context)

def Resume(request):
    vac_n = Vacancy.objects.get(id=id)
    context = {'vacancy': vac_n}
    return render(request, 'resume.html', context)

