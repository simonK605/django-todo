import django_filters

from .models import *

class TodoFilter(django_filters.FilterSet):
    class Meta:
        model = Todo
        fields = '__all__'