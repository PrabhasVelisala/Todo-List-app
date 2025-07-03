from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
import datetime


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your main page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Home view: Add new task for logged-in user
@login_required
def home(request):
    success = False
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        updated_at = datetime.datetime.now()
        # Create task associated with current user
        Task.objects.create(
            taskTitle=title,
            taskDesc=desc,
            time=updated_at,
            user=request.user
        )
        success = True
    context = {'success': success}
    return render(request, 'index.html', context)

# View to list tasks for logged-in user
@login_required
def tasks(request):
    user_tasks = Task.objects.filter(user=request.user)
    if user_tasks.exists():
        context = {'tasks': user_tasks}
        return render(request, 'tasks.html', context)
    else:
        return HttpResponse("<h2 class='textcenter'>Your list is empty. Add some tasks in home and get back to this page.</h2>")

# Delete a task (only if it belongs to the logged-in user)
@login_required
def delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('tasks')  # Or render 'tasks.html' if preferred

# Edit task view
@login_required
def edit(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.taskTitle = request.POST.get('title')
        task.taskDesc = request.POST.get('desc')
        task.time = datetime.datetime.now()
        task.save()
        return redirect('tasks')
    else:
        context = {
            'title': task.taskTitle,
            'desc': task.taskDesc,
            'id': task.id
        }
        return render(request, 'edit.html', context)

# Update task (handled within edit view after POST)
# Alternatively, you can keep separate update view if preferred


def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        import datetime
        updated_at=datetime.datetime.now()
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc, time=updated_at)
        ins.save()
        context = {'success':True}    
        
    return render(request, 'index.html', context)

def tasks(request):
    if Task.objects.all():
        allTasks = Task.objects.all()
        context ={'tasks':allTasks}
        return render(request, 'tasks.html', context)
    else:
        return HttpResponse("<h2 class=\"textcenter\"> your list is empty add some tasks in home and get back to this page")

def delete(request,id):
    obj = Task.objects.get(id=id)
    obj.delete()
    allTasks = Task.objects.all()
    context ={'tasks': allTasks}
    return render(request, 'tasks.html', context)

def edit(request,id):
    task = get_object_or_404(Task, id=id)
    mydictionary = {
        'title': task.taskTitle,
        'desc': task.taskDesc,
        'id': task.id
    }
    return render(request, 'edit.html', context=mydictionary)

def update(request,id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.taskTitle = request.POST.get('title')
        task.taskDesc= request.POST.get('desc')
        import datetime
        updated_at = datetime.datetime.now()
        task.time=updated_at
        # update other fields as needed
        task.save()
        
        return redirect('/tasks')

