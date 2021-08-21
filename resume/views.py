from django.shortcuts import render, redirect
from django.core.mail import send_mail


def home(request):
    return render (request, 'index.html', {})


def contactme(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'Website inquiry from ' + name, 
            message, 
            email, 
            ['djangotest960@gmail.com'],
        )
             
        return render (request, 'contact.html', {'name' : name})
    
    else:
        return render (request, 'contact.html', {})
        
