from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo.index'),
    path('/<int:id>', views.show, name='todo.show'),
    path('/store', views.store, name='todo.store'),
    path('/delete/<int:id>', views.delete, name='todo.delete'),
    path('/finish/<int:id>', views.finish, name='todo.finish'),
]
