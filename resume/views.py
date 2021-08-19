from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Profile, Work_Experience, Education, Internships, Portfolio,Technical_skills, Soft_skills
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect



def home(request):
    return render (request, 'index2.html', {})
    #return render (request, 'index.html', {})
   

def profile_view(request):
    context = RequestContext(request)
    profile_list = Profile.objects.all()
    context_dict = {'profiles': profile_list}
    return render('index2.html',context_dict, context)



def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        return redirect('home')
    else:
        return render(request, "index.html", {'form': form})

# def contact(request):
    
#     if request.method == 'GET':
#         form = ContactForm()

#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             #form.save()
#             #return HttpResponseRedirect('/')
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             try:
#                send_mail(name, message, email, ['admin@example.com'])
#             except BadHeaderError:
#                return HttpResponse('Invalid header found')
#             return redirect ('success')
            
#     return render(request, "index.html", {'form': form})

# def message_received(request):
#    #return HttpResponse('Thanks for your message. I will contact you within 24 hours')
#    return render (request, 'success.html', {})

