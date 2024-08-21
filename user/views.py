from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def register(request):

    c = {}

    if request.method == 'POST':

        username = request.POST.get('u')
        email = request.POST.get('e')
        password = request.POST.get('p')

        user = User(username = username)
        user.set_password(password)
        user.email = email
        user.save()

        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('/register2')

    return render(request, 'register1.html', c)


def register2(request):

    c = {}

    return render(request, 'register2.html', c)