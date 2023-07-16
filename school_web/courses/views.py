from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Queries1Form, Queries2Form, Queries3Form
from .models import Queries3


def directions(request):
    return render(request, 'courses/directions.html')


def entryForm(request):
    category_id = request.GET.__getitem__('category')
    if request.method == 'GET':
        if category_id == '1':
            form = Queries1Form()
            data = {
                'form': form
            }
            return render(request, 'courses/entryForm1.html', data)
        elif category_id == '2':
            form = Queries2Form()
            data = {
                'form': form
            }
            return render(request, 'courses/entryForm2.html', data)
        else:
            return redirect('home')

    if request.method == 'POST':
        if category_id == '1':
            form = Queries1Form(request.POST)
            if form.is_valid():
                form.save()
        if category_id == '2':
            form = Queries2Form(request.POST)
            if form.is_valid():
                form.save()
        return redirect('home')


def grade_info(request):
    return render(request, 'courses/grade_buttons.html')


def entryFormSchool(request):
    category_id = request.GET.__getitem__('category')
    if request.method == 'GET':
        form = Queries3Form()
        data = {
            'form': form,
            'num': category_id
        }
        return render(request, 'courses/entryForm3.html', data)

    if request.method == 'POST':
        form = Queries3Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
