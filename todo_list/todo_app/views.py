from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import datetime

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})

def create_task(request):
    title = request.POST['txtTitle']
    description = request.POST['txtDescription']
    # Convertir la fecha a formato datetime
    date_str = request.POST['txtDate']
    date = datetime.fromisoformat(date_str.replace('T', ' '))
    # El checkbox solo se envía si está marcado, si no está marcado no aparece en POST
    completed = 'Status' in request.POST
    
    Task.objects.create(
        title=title, 
        description=description, 
        completed=completed,
        date=date)# Usar la fecha actual como fecha de realización
    return redirect('/')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST['txtTitle']
        description = request.POST['txtDescription']
        date_str = request.POST['txtDate']
        date = datetime.fromisoformat(date_str.replace('T', ''))
        completed = 'Status' in request.POST
        task.save()
        return redirect('/')
    return render(request, "task_list.html", {'task': task})
       

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')