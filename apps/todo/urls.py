from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo.index'),
    path('/<int:id>', views.show, name='todo.show'),
    path('/store', views.store, name='todo.store'),
]
