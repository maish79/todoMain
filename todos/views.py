from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import *
from .forms import *

# Create your views here.

def home(request):
    lists = list.objects.all()

    form = listForm()

    if request.method == 'POST':
        form = listForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'lists': lists, 'form':form}
    return render(request, 'tasks/list.html', context)

def addTask(request, pk):
    task = list.objects.get(id=pk)

    form = listForm(instance=task)
    if request.method == 'POST':
        form = listForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'tasks/add.html', context)

def deleteTask(request, pk):
    item = list.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)