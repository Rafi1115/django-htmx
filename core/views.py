from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .models import Todo
from .forms import TaskForm


def task_list(request):
    todo = Todo.objects.all()

    return render(request, 'task_list.html', {'todo':todo})

def display_tasks(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            task = form.save(commit=False)
            t = request.POST.get("name")
            if Todo.objects.filter(name=t).exists():
                print('not adding anything you type')
            else:

                # task.user = request.user
                task.save()
    todo = Todo.objects.all()
    return render(request, 'todo.html', {'todo': todo, 'form':form})


def check(request):
    taskname = request.POST.get("name")

    if Todo.objects.filter(name=taskname):
        return HttpResponse("<div style='color:red'>This task already exist <div>")
    else:
        return HttpResponse("<div style='color:green'>This task not exist <div>")


class TodoList(generic.ListView):
    model = Todo
    template_name = "todolist.html"
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Todo.objects.all()
        return context

def add_todo(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            task = form.save(commit=False)
            name = request.POST.get("name")
            if Todo.objects.filter(name=name).exists():
                print('not adding anything you type')
            else:
                # task.user = request.user
                task.save()
    todo = Todo.objects.all()
    return render(request, 'todo.html', {'todo': todo, 'form':form})

def delete_todo(request, pk):
    dele = Todo.objects.filter(id=pk).delete()
    todo = Todo.objects.all()
    return render(request, 'todo.html', {'todo':todo})

def complete_todo(request, pk):
    dele = Todo.objects.filter(id=pk)
    print(dele.values(), 'printing current value')
    for i in dele:
        i.completed = True
        i.save()
   
    todo = Todo.objects.all()
    return render(request, 'todo.html', {'todo':todo})

def undo_todo(request, pk):
    dele = Todo.objects.filter(id=pk)
    print(dele.values(), 'printing current value')
    for i in dele:
        i.completed = False
        i.save()
    todo = Todo.objects.all()
    return render(request, 'todo.html', {'todo':todo})

def edit_todo(request, pk):
    todo = Todo.objects.all()
    question = Todo.objects.get(id=pk)
    form = TaskForm(request.POST, instance=question)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:after_edit')
    return render(request, 'edit.html', {'todo':question, 'form':form})

def after_edit(request):
    todo = Todo.objects.filter()
    return render(request, 'edit_back.html', {'todo':todo})
    

def get_task(request):
    task = Todo.objects.all()
    return render(request, 'htmx.html', {'todo': task})
 

