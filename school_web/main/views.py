from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')
def online_info(request):
    return render(request, 'main/online_info.html')