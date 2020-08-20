from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def home(request):
    if request.method == "POST":
        print("request: ", request.method)
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = Todo.objects.create(task_name=form.cleaned_data['task_name'])
            todo.save()
    else:
        form = TodoForm()

    list_tasks_already_do = Todo.objects.filter(is_doing=True)
    list_tasks_todo = Todo.objects.filter(is_doing=False)

    return render(request, "todo/index.html", locals())



    
    
