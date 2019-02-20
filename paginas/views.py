from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def inicial(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = settings.EMAIL_HOST_USER
            nome = form.cleaned_data['nome']
            message = "%s\n%s\n%s" % (nome, from_email,form.cleaned_data['message'])
            try:
                send_mail(subject, message, from_email,['renan.bisposilva@gmail.com','RENAN_3022830@trt5.jus.br','renatabastos@live.com'], fail_silently=True,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/suces')
    return render(request, "index.html", {'form': form})

def email_suces(request):
    return render(request,"suces.html")

