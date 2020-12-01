from django.shortcuts import render
from .models import Task
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import TaskAddForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required
def tasks_all(request):     # sortowanie po deadline
    tasks = Task.objects.all()
    status_ongoing = Task.objects.filter(status='ongoing')
    return render(request, 'tasks_all.html', {'tasks' : tasks, 'status_ongoing': status_ongoing})

@login_required
def task_add(request):
    form = TaskAddForm
    if request.method == 'POST':
        form = TaskAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Pomyślnie dodano zadanie')
    return render(request, 'task_add.html', {'form' : form})

@login_required
def task_delete(request, title):
    task = get_object_or_404(Task, title=title)
    task_delete = Task.objects.filter(title=title).delete()
    tasks = Task.objects.all()
    messages.add_message(request, messages.INFO, 'Pomyślnie usunięto zadanie')
    return render(request, 'task_deleted.html', {'task' : task,
                                              'task_delete' : task_delete,
                                                 'tasks' : tasks})

@login_required
def task_detail(request, title):
    task = get_object_or_404(Task, title=title)
    return render(request, 'task_detail.html', {'task' : task })


def logout_view(request):
    return render(request, 'logout.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.add_message(request, messages.INFO, 'Rejestracja przebiegła pomyślnie.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def home(request):
    return render(request, 'home.html')




