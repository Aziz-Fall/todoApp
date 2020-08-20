from django.db import models

# Create your models here.

class Todo(models.Model):

    task_name = models.CharField(verbose_name="task's name", max_length=50)
    is_doing = models.BooleanField(default=False)
    date = models.DateField(verbose_name="task's date", auto_now_add=True)

    class Meta:
        verbose_name = "todo"
        ordering=['date']
        verbose_name_plural = "todos"

    def __str__(self):
        return self.task_name

