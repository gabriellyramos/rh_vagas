from django.shortcuts import render, redirect, reverse

def login(request):
    context = {}
    return render(request, 'login.html', context)