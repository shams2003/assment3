from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request,'index.html')

def home (request) :
    return render (request,'hme.html' )

def about (request) :
    return render (request,'about.html' )

def show (request) :
    return render (request,'show.html' )

