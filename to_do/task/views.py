from django.shortcuts import render, HttpResponse, redirect
from task.models import Task

# Create your views here.


def home(request):
    tasks = Task.objects.all()
    context = {
        'task_list': tasks
        }
    return render(request, 'task/home.html', context=context)


def task_detail(request, task_id):

    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('home/')

    return render(request, "task/task_view.html", context={'task': task})


def task_delete(request, task_id):

    try:
        Task.objects.filter(id=task_id).delete()
    except Task.DoesNotExist:
        return redirect('/home/')
    return redirect('/home/') # ?if the first slash is removed, it is redirected to i.e task-delete/id/home


def task_update(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('home/')
    return render(request, 'task/task_update.html', context={'task': task})


def task_create(request):

    return render(request, 'task/new_task.html')

