from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo.index'),
    path('/<int:id>', views.show, name='todo.show'),
    path('/store', views.store, name='todo.store'),
    path('/edit/<int:id>', views.edit, name='todo.edit'),
    path('/update/<int:id>', views.update, name='todo.update'),
    path('/delete/<int:id>', views.delete, name='todo.delete'),
    path('/finish/<int:id>', views.finish, name='todo.finish'),
]
