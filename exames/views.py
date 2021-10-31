from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def exame(request):
    return render(request, 'exame.html')

