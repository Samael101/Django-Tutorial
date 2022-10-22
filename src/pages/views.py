from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *arg, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Hello World<h1>")
    return render(request, 'home.html', {})

def Contact_view(request, *arg, **kwargs):
    print(request.user)

    return render(request, 'contact.html', {})

def about_view(request, *arg, **kwargs):
    my_context={
        "title" : "abc This is about me",
        "my_number" : 123,
        "my_list": [123,4242,312,"ABC"],
        "my_html": "<h1>Hello World</h1>",
    }

    return render(request, 'about.html', my_context)

def Social_view(request, *arg, **kwargs):
    return HttpResponse("<h1>Social<h1>")
    # return render(request, 'home.html', {})

