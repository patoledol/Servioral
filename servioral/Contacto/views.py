from email import message
import imp
from datetime import date, datetime
from time import strptime
from django.shortcuts import render, redirect
from django.urls import reverse
from Contacto.forms import ContactoForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# Create your views here.

def send_email(mail, name, subject):
    context = {'name': name, 'subject': subject}
    template = get_template('Contacto/email.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'ServiOral',
        'Soy ServiOral',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email_self = EmailMultiAlternatives(
        'ServiOral',
        'Soy ServiOral',
        settings.EMAIL_HOST_USER,
        ["servioral.pacientes@gmail.com"]
    )
    email.attach_alternative(content, 'text/html')
    email.send()
    email_self.attach_alternative(content, 'text/html')
    email_self.send()

def contacto(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    subject = request.POST.get('subject')
    if request.method == "POST":
        form = ContactoForm(request.POST)
        send_email(email, name, subject)
        if form.is_valid():
            form.save()
    else:
        form = ContactoForm()
    context = {
        'form':form,
    }
    return render(request, "Contacto/contact.html", context)
      
