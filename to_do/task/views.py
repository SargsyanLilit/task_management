from django.shortcuts import render, HttpResponse, redirect
from task.models import Task
from task.forms import TaskForm, TaskUpdate, TaskUpdateForm

# Create your views here.


def home(request):
    tasks = Task.objects.all().order_by('-created_at')
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
        return redirect('home')
    return redirect('home')


def task_update(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('home')

    update_form = TaskUpdate(instance=task)

    if request.method == 'POST':
        update_form = TaskUpdate(request.POST, instance=task)
        if update_form.is_valid():
            update_form.save()
            return redirect('home')

    context = {
        "form": update_form,
    }

    return render(request, 'task/task_update.html', context=context)


def task_create(request):
    create_form = TaskForm()
    if request.method == 'POST':
        # print(request.POST)
        create_form = TaskForm(request.POST)
        if create_form.is_valid():
            # Task.object.create(**create_form.cleaned_data)
            # print(create_form.cleaned_data)
            name = create_form.cleaned_data['name']
            description = create_form.cleaned_data['description']
            status = create_form.cleaned_data['status']
            Task.objects.create(name=name, description=description, status=status)
            return redirect('home')

    context = {
        'form': create_form
         }
    return render(request, 'task/new_task.html', context=context)


# class version
def task_update_form(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('home')

    data = dict(name=task.name, description=task.description, status=task.status)

    update_form = TaskUpdateForm(data=data)

    if request.method == 'POST':
        update_form = TaskUpdateForm(request.POST)
        if update_form.is_valid():
            task.status = update_form.cleaned_data['status']
            task.description = update_form.cleaned_data['description']
            task.save()
            return redirect('home')

    context = {
        "form": update_form,
    }

    return render(request, 'task/task_update.html', context=context)


# class version
def task_create_model_form(request):
    create_form = TaskUpdate()
    if request.method == 'POST':
        # print(request.POST)
        create_form = TaskUpdate(request.POST)
        if create_form.is_valid():
            # Task.object.create(**create_form.cleaned_data)
            # print(create_form.cleaned_data)

            # name = create_form.cleaned_data['name']
            # description = create_form.cleaned_data['description']
            # status = create_form.cleaned_data['status']
            # Task.objects.create(name=name, description=description, status=status)
            create_form.save()
            return redirect('home')

    context = {
        'form': create_form
    }

    return render(request, 'task/new_task.html', context=context)

