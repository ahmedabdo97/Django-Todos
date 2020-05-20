from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.


def todo_list(request):
    todo = Todo.objects.all()
    context = {
        "todo_list": todo
    }
    return render(request, "todo_list2.html", context)  # for global package
    # return render(request, "todo/todo_list.html") for in todo app template internally


def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo_detail.html", context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "todo_create.html", context)


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "todo_update.html", context)


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
