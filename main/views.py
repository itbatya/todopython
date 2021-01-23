from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list" : todo_list})

def second(request):
    return HttpResponse('test 2 page')

def third(request):
    return HttpResponse('This is page test3')


def added(request):
    return render(request, "added.html")

def changed(request):
    return render(request, "changed.html")

def deleted(request):
    return render(request, "deleted.html")


def add_todo(request):
    data = request.POST
    text = data["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect(test)