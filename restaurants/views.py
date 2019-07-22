from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunction(request):
    context = {
        "msg": "Hello World!",
    }
    return render(request, 'page.html', context)
