from django.shortcuts import render, get_object_or_404

from .models import *

def profile_view(request, username):

    c = {}

    profile = get_object_or_404(Profile, user__username=username)
    links = Link.objects.filter(profile = profile)

    return render(request, 'linktree/profile.html', c)