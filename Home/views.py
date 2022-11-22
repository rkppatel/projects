from django.http import HttpResponse
from smtplib import SMTPResponseException
from django.shortcuts import render
from Home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


'''def index(request):
    return HttpResponse("This is homepage.")'''


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def pricing(request):
    return render(request, 'pricing.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        example = request.POST.get('example')
        contact = Contact(name=name, email=email, example=example)
        contact.save()
        messages.success(request, 'Profile details updated.')
    return render(request, 'contact.html')
