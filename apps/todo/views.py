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
    points_sum = Todo.objects.aggregate(points_sum=Sum('point_id__value'))['points_sum']

    return render(request, 'todo/index.html', {
        'todos': todos,
        'points_sum' : points_sum
    })


def show(request, id):
    todo = get_object_or_404(Todo, id=id)

    return render(request, 'todo/show.html', {
        'todo': todo
    })

def store(request):
    form = TodoForm(request.POST)
    point = Point.objects.create(value=request.POST['point'])

    if point:
        if form.is_valid():
            todo = form.save(commit=False)
            todo.point_id = point
            todo.save()


    return redirect('todo.index')