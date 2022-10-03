from django.shortcuts import render


def index(request):
    template = 'main.html'
    return render(request, template)