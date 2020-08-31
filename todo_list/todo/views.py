from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from .forms import TodoForm

def home(request):
    """
        Check the request method 
            if it is POST, Recover data and check them
            else return an empy form
    """
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid(): # check if the form is valid 
            task_name = form.cleaned_data['task_name']
            print("Form is valid ..., task name : ", task_name)
            # Create and save the data in the data base
            todo = Todo.objects.create(task_name=form.cleaned_data['task_name'])
            todo.save()
    else:
        form = TodoForm()

    # Recover the list of tasks already do
    list_tasks_already_do = Todo.objects.filter(is_doing=True)
    
    # Recover the list of tasks to do
    list_tasks_todo = Todo.objects.filter(is_doing=False)
    
    return render(request, "todo/index.html", locals())

def delete(request, pk):
    # Recover the task and return the delete task page
    task = get_object_or_404(Todo, pk=pk)
    return render(request, "todo/delete_task.html", locals())

def delete_task(request, pk):
    # Recover, delete task by his id
    task = get_object_or_404(Todo, pk=pk)
    task.delete()
    print("task: ", task)

    # Redirect to the home page
    return HttpResponseRedirect(reverse('home'))


def task_done(request, pk):
    # Recover the task by his id and put it done
    task = get_object_or_404(Todo, pk = pk)
    task.is_doing = True
    task.save()

    # Redirect to the home page
    return HttpResponseRedirect(reverse('home'))



    
    
