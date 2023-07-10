from django.shortcuts import render, redirect
from .forms import QueriesForm

def directions(request):
    return render(request, 'courses/directions.html')


def entryForm(request):
    if request.method == 'POST':
        form = QueriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = QueriesForm()

    data = {
        'form': form
    }

    return render(request, 'courses/entryForm.html', data)
