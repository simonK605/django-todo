from django.shortcuts import render
from django.db.models import Sum

# Models
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    points_sum = Todo.objects.aggregate(points_sum=Sum('point_id__value'))['points_sum']

    return render(request, 'todo/index.html', {
        'todos': todos,
        'points_sum' : points_sum
    })


def show(request, id):
    todo = Todo.objects.get(id=id)

    return render(request, 'todo/show.html', {
        'todo': todo
    })