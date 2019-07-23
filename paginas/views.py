# from django.shortcuts import render
# from django.conf import settings
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from .forms import ContactForm
# import json


# def inicial(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     # else:
#     #     form = ContactForm(request.POST)
#     #     if form.is_valid():
#             # subject = form.cleaned_data['subject']
#             # from_email = settings.EMAIL_HOST_USER
#             # nome = form.cleaned_data['nome']
#             # message = "%s\n%s\n%s" % (nome, from_email,form.cleaned_data['message'])
#             # try:
#             #     send_mail(subject, message, from_email,['renan.bisposilva@gmail.com','RENAN_3022830@trt5.jus.br','renatabastos@live.com'], fail_silently=True,)
#             # except BadHeaderError:
#             #     return HttpResponse('Invalid header found.')
#             # return redirect('/suces')
#         return render(request, "index.html", {'form': form})

#     if request.method == "POST" :
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         form = ContactForm(body)
#         print(body)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             nome = form.cleaned_data['nome']
#             message = "%s\n%s\n%s" % (nome, from_email,form.cleaned_data['message'])
#             try:
#                 send_mail(subject, message, from_email,['renan.bisposilva@gmail.com','renatabastos@live.com'], fail_silently=True,)
#             except BadHeaderError:
#                 return HttpResponse(
#             json.dumps("Falha"),
#             content_type= 'application/json',
#             status= 500
#         )
#             return HttpResponse(
#             json.dumps("OK"),
#             content_type= 'application/json',
#             status= 200
#         )
#         return HttpResponse(
#             json.dumps("Erro interno no servidor"),
#             content_type= 'application/json',
#             status= 500
#         )


from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render, redirect
from .forms import ContactForm, NumForm, EmailForm
from django.http import JsonResponse
import urllib.parse


def inicial(request):
    if request.method == 'GET':
        form = ContactForm()
        numForm = NumForm()
        emailForm = EmailForm()

    else:
        form = ContactForm(request.POST)
        if form.is_valid():    
            subject = form.cleaned_data['subject']
            from_email = settings.EMAIL_HOST_USER
            nome = form.cleaned_data['nome']
            message = "%s\n%s\n%s" % (nome, from_email,form.cleaned_data['message'])
            try:
                send_mail(subject, message, from_email,['renan.bisposilva@gmail.com','RENAN_3022830@trt5.jus.br','renatabastos@live.com'], fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/suces')
        else:
            numForm = NumForm(request.POST)
            if numForm.is_valid():
                subject = "Pediu contato"
                from_email = settings.EMAIL_HOST_USER
                nome = "Pediu contato"
                message = "%s\n%s\n%s" % (nome, from_email,numForm.cleaned_data['fone'])
                try:
                    send_mail(subject, message, from_email,['renan.bisposilva@gmail.com','RENAN_3022830@trt5.jus.br','renatabastos@live.com'], fail_silently=False,)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('/suces')
            else:
                emailForm = EmailForm(request.POST)
                print(type(request.POST))
                if emailForm.is_valid():
                    subject = "Pediu contato"
                    from_email = settings.EMAIL_HOST_USER
                    nome = "Pediu contato"
                    message = "%s\n%s\n%s" % (nome, from_email,emailForm.cleaned_data['email'])
                    try:
                        send_mail(subject, message, from_email,['renan.bisposilva@gmail.com','RENAN_3022830@trt5.jus.br','renatabastos@live.com'], fail_silently=False,)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect('/suces')

    return render(request, "index.html", {
        'form': form,
        'numForm' : numForm,
        'emailForm' : emailForm
    })

def email_suces(request):
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
                send_mail(subject, message, from_email,['renan.bisposilva@gmail.com','RENAN_3022830@trt5.jus.br','renatabastos@live.com'], fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/suces')
                    
    return render(request,"suces.html", {
        'form': form
    })

def valido(request):
    body_unicode = request.body.decode('utf-8')
    numForm = NumForm(QueryDict(body_unicode))
    emailForm = EmailForm(QueryDict(body_unicode))
    form = ContactForm(QueryDict(body_unicode))
    if (request.is_ajax()):
        if numForm.is_valid():
            return JsonResponse({
                'fone':True,
                'email' : False,
                'mensagem' : False
            })

        if emailForm.is_valid():
            return JsonResponse({
                'fone':False,
                'email' : True,
                'mensagem' : False
            })

        if form.is_valid():
            return JsonResponse({
                'fone':False,
                'email' : False,
                'mensagem' : True
            })

        return JsonResponse({
            'fone':False,
            'email' : False,
            'mensagem' : False
        })