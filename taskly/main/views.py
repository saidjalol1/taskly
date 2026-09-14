from django.shortcuts import render
from .models import CategoryTask, Task
from datetime import datetime




def main_view(request):
    context = {
        "categories": CategoryTask.objects.all()
    }

    today = datetime.now()

    dues_today = Task.objects.filter(due__day=today.day)

    context["todays"] = dues_today

    return render(request, 'index.html', context)