from django.shortcuts import render

def landing(request):

    c = {}

    return render(request, 'landing.html', c)