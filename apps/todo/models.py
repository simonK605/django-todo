from django.db import models


class Point(models.Model):
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.value)
    

class Todo(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    point_id = models.ForeignKey(Point, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name