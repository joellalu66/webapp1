from django.shortcuts import render
from django.http import HttpResponse


def display(req):
    return render(req,'index.html')