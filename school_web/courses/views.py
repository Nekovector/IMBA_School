from django.shortcuts import render


def directions(request):
    return render(request, 'courses/directions.html')