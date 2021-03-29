from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.contrib import messages


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            try:
                send_mail(subject, f'from : {name} \n  email  : {from_email}  \n  message : {message}', from_email, ['elmezianimohamed45@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "merci, le message à été bien envoyer")
            return redirect('contact')
            
    return render(request, "index.html", {'form': form})

# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')


# def index(request):
#     context = {}
#     return render(request , 'index.html' , context)