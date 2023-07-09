from django.shortcuts import render


def directions(request):
    return render(request, 'courses/directions.html')


def entryForm(request):
    if request.method == 'POST':
        post_data = request.POST
        subjects = list()
        for key in post_data:
            if post_data[key] == "on":
                subjects.append(key)
        data = {"subjects": subjects}
        return render(request, 'courses/entryForm.html', context=data)
    else:
        return render(request, 'courses/entryForm.html')
