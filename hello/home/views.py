from cgitb import html
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    ctx = {
        'sid':"Siddhartha Industries",
        'lst': [1,2,3],
        "img": ['https://i.imgur.com/QISZALg.jpeg','https://i.imgur.com/1uXgW1a.jpeg','https://i.imgur.com/Re0F7md.jpeg' ]
        }
    return render(request,'index.html',ctx)

def about(request):
    return HttpResponse("<h1>about</h1>")

def services(request):
    return HttpResponse("<h1>serv</h1>")

def contact(request):
    return HttpResponse("<h1>con</h1>")

def login(request):
    context ={'org':'Siddhartha Industries'}
    return render(request, 'login.html', context)
