from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request, "helloworld.html", {"name": "ivan"})

# Create your views here.
# requests -> response
# request handler