from django.shortcuts import render
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, redirect

# Models
from .models import Todo
from .models import Point

# Forms
from .forms import TodoForm


def index(request):
    todos = Todo.objects.all()
    points_sum = Todo.objects.filter(done=True).aggregate(points_sum=Sum('point_id__value'))['points_sum']

    return render(request, 'todo/index.html', {
        'todos': todos,
        'points_sum' : points_sum,
        'points': Point.objects.order_by('value')
    })


def show(request, id):
    todo = get_object_or_404(Todo, id=id)

    return render(request, 'todo/show.html', {
        'todo': todo
    })


def store(request):
    form = TodoForm(request.POST)
    print(request.POST)
    print(form.is_valid())
    if form.is_valid():
        todo = form.save()

    return redirect('todo.index')


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()

    return redirect('todo.index')


def finish(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.done = not todo.done
    todo.save()
    return redirect('todo.index')
