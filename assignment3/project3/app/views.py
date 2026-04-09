from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "app/index.html")


def result(request):
    if request.method =="POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        language = request.POST.get('language')
        comment = request.POST.get('comment')

        context = {
            'name': name,
            'location': location,
            'language': language,
            'comment': comment,
        }
        return render(request, 'app/result.html', context)