from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import CategoryTask, Task
from datetime import datetime



@login_required
def main_view(request):
    context = {
        "categories": CategoryTask.objects.all()
    }

    today = datetime.now()

    dues_today = Task.objects.filter(due__day=today.day)
    others = Task.objects.exclude(due__day=today.day)

    context["todays"] = dues_today
    context['others'] = others

    return render(request, 'index.html', context)


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get('due_date')
        category_id = request.POST.get('category_id')


        new_task = Task.objects.create(
            name = title,
            due = date,
            category_id = category_id
        )
        new_task.save()


    return redirect('main:asosiy')

@login_required
def delete_post(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = Task.objects.get(id = task_id)
        task.delete()

    return redirect("main:asosiy")

@login_required
def toggle_task_status(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        print(task_id)
        task = Task.objects.get(id = task_id)

        task.status = not task.status
        task.save()
        
    return redirect("main:asosiy")


def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request=request, username=username, password=password)

        if user is None:
            messages.error(request, "Sening parol yoki Foydalanuvchi noming no to'gri")
            return render(request, "login.html")

        login(request, user)
        messages.success(request, "Hush kelibsiz !")
        return redirect("main:asosiy")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("main:login_page")