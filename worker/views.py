from django.shortcuts import render, redirect, HttpResponse
from worker.models import Worker, Resume
from .forms import ResumeEditForm


def workers(request):
    workers = Worker.objects.all()
    context = {"workers": workers}
    return render(request, 'workers.html')

def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    # SELECT * FROM Worker WHERE id={id}
    context = {'worker': worker_object}
    return render(request, 'worker.html', context)

def resume_list(request):
    resume_query = Resume.objects.all()
    return render(
        request, 'resume/resume_list.html',
        {"resumes": resume_query}
    )



def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)
    return render(
        request, 'resume/resume_detail.html',
        {'resume': resume_object}
    )


def resume_edit(request, id):
    resume_object = Resume.objects.get(id=id)

    if request.method == "GET":
        form = ResumeEditForm(instance=resume_object)
        return render(request, "resume/resume_edit.html", {"form": form})

    elif request.method == "POST":
        form = ResumeEditForm(
            data=request.POST,
            instance=resume_object,
            files=request.FILES
        )
        if form.is_valid():
            obj = form.save()
            return redirect(resume_info, id=obj.id)
        else:
            return HttpResponse("Форма не валидна")



def my_resume(request):
    if request.user.is_authenticated:
        resume_query = Resume.objects.filter(worker=request.user.worker)
        # resume_query = request.user.worker.resume.all()
        return render(
            request, 'resume/resume_list.html',
            {"resumes": resume_query}
        )
    else:
        return redirect('home')

def vac_description(request, id):
    vacancy_object = Vacancy.objects.get(id=id)
    candidates = vacancy_object.candidates.all()
    context = {
        'vacancy': vacancy_object,
        'candidates': candidates,
    }
    return render(request, 'vac_description.html', context)


def add_resume(request):
    template = 'resume/resume_add.html'
    if request.method == "GET":
        # показать форму
        return render(request, template)
    elif request.method == "POST":
        # записать резюме в БД
        new_resume = Resume()
        new_resume.worker = request.user.worker
        new_resume.title = request.POST["form-title"]
        new_resume.text = request.POST["form-text"]
        new_resume.save()
        return HttpResponse("Запись добавлена!")


def create_resume(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')
        else:
            form = ResumeAddForm()
            return render(request,
                          'create_resume.html',
                          {'form': form}
            )






