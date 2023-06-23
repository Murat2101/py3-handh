from django.shortcuts import render, HttpResponse
from .models import Vacancy, Company

def homepage(request):
    return render(request=request, template_name="index.html")

def about(request):
    return HttpResponse('Найдите работу или работника мечты!')

def contact_view(request):
    return HttpResponse('''
        <div>
            Phone: +3874628734 <br>
            Email: kaium@gmail.com
        </div>
    ''')

def vacancy_list(request):
    vacancies = Vacancy.objects.all() # select в django ORM
    context = {"vacancies": vacancies} # context data для jinja2
    return render(request,'vacancies.html',context)

def company_list(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'companies.html', context)
