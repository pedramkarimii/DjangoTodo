from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreatForm, TodoUpdateForm
# Create your views here.
# ADD HttpResponse
# from django.http import HttpResponse
# def say_hello(request):
#     return HttpResponse('Hello World')


def main_say_hello(request):
    all = Todo.objects.all()
    return render(request, 'main.html', context={'todo': all})
    # show_name = {"name": "pedram"}
    # return render(request, 'main.html', context=show_name)
    # or
    # return render(request, 'main.html', context={"name" : "pedram"})
    # or
    # return render(request, 'main.html', {"name" : "pedram"})


def say_hello(request):
    return render(request, 'index.html')


def detail(request, TODO_ID):
    todo = Todo.objects.get(id=TODO_ID)
    return render(request, 'detail.html', context={'todo': todo})


def delete(request, TODO_ID):
    Todo.objects.get(id=TODO_ID).delete()
    messages.success(request, "Todo deleted successfully",  extra_tags="success")
    return redirect("home")

def update(request, TODO_ID):
    todo = Todo.objects.get(id=TODO_ID)
    todo_form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        todo_form = TodoUpdateForm(request.POST, instance=todo)
        if todo_form.is_valid():
            todo_form.save()
            messages.success(request, "Todo updated successfully", extra_tags="success")
            return redirect( "detail", TODO_ID)
    else:
        todo_form = TodoUpdateForm(instance=todo)
    return render(request, 'update_todo.html', context={'todo_form': todo_form})


def creat_todo(request):
    if request.method == "POST":
        todo_form = TodoCreatForm(request.POST)
        if todo_form.is_valid():
            cd = todo_form.cleaned_data
            # title-> model , cd['title'] -> form
            Todo.objects.create(title=cd['title'], description=cd['description'],create=cd['create'], completed=cd['completed'])
            messages.success(request, "Todo deleted successfully", extra_tags="success")
            return redirect("home")
    else:
        todo_form = TodoCreatForm()

    return render(request, 'creat_todo.html', context={'todo_form': todo_form})