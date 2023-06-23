from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home_render(request):

    return render(request, 'home.html')
