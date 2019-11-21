from django.shortcuts import render


def Hello(request):
    return render(request, 'track/helloworld.html')


def About(request):
    return render(request, 'track/about.html')
