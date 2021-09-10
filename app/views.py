from .models import FAQ, Service
from django.shortcuts import render,HttpResponse
 

# Create your views here.
def home(request):
    posts = Service.objects.all()
    fs = FAQ.objects.all()
    if fs:
        print(fs)

    context = {"fs":fs, "posts":posts}
    return render(request, "index.html", context)
