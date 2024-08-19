from django.shortcuts import redirect, render, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required
def task_lists(request):

    tasks = Task.objects.all()

    return render(request, "task_list.html", {"tasks": tasks})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) #this creates a 'Task' object from the valid form but does not save it to the database immediately.
            task.created_by = request.user #this assigns the current logged-in user as the creator of the task
            task.assigned_to = request.user #this assigns the task to the same user who created it
            task.save()

            return redirect('task')

    else:
        form = TaskForm()

    return render(request, "create.html", {"form": form})


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task") 
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'create.html', {"form": form})



def delete_task(request, task_id):
    task = get_object_or_404(Task, id= task_id, created_by=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task")

    return render(request, "delete.html", {"task": task})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) #creates an instance of 'UserCreationForm' with the data that the user submitted 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #after saving the user, this line retrieves the username from the cleaned form data. 'cleaned_data' is a dictionary containing the validated form data
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #checks the informations provided against the user database to verify the user. if the info are correct, it returns a 'User' object, otherwise, it returns 'None'
            login(request, user) #if a 'User' object is returned, the newly created user is logged in
            return redirect('task')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
    

def logout_view(request):
    logout(request)
    return redirect('login')


def password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Password_changed_successfully')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset.html', {'form': form})





