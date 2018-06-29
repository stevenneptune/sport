from django.shortcuts import render
from django.http import request
# Create your views here.

def index(request):
    return render(request,'index.html')

def piayers(request):
    return render(request,'players.html')


def team(request):
    return render(request,'team.html')

def details(request):
    return render(request,'details.html')

def match(request):
	return render(request,'match.html')