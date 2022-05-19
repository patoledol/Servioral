from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from Cita.forms import CitaForm
from Cita.models import cita
from Odontologo.models import odontologo
from Especialidad.models import especialidad
from Paciente.models import paciente
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
# Create your views here.

def home(request):
    email = request.POST.get('email')
    name = request.POST.get('paciente')
    date_final = request.POST.get("date")
    final_hour = request.POST.get("hour")
    citas = cita.objects.all()
    if request.method == "POST":
          form = CitaForm(request.POST)
          print(request.POST.get("date"))
          print(request.POST.get("hour"))
          if form.is_valid():
            today = datetime.today()
            date1 = request.POST.get("date")
            date2= datetime.strptime(date1, '%Y-%m-%d')
            doctor1 = request.POST.get("id_doc")
            doctor2 = odontologo.objects.get(id_odontologo=doctor1)
            doctor4 = odontologo.objects.get(id_odontologo=doctor1)
            if date2 < today:
                  return redirect(reverse('home')+ "?fecha-no-valida")
            elif cita.objects.filter(id_doc = doctor2):
                  print("Hola")
            if cita.objects.filter(date=date2):
                  print("Hola 2")
                  return redirect(reverse('home')+ "?no-disponible")
            else:
                  form.save() 
                  send_email(email, name, doctor4, date_final, final_hour)
            return redirect(reverse('home')+ "?ok")
    else:
          form = CitaForm()
 
    context = {
          "form":form,
          "citas": citas,
    }
    
    return render(request, "core/index.html", context)

def send_email(mail, name, doctor4, date_final, final_hour):
    context = {'name': name, 'doctor': doctor4, 'date': date_final, 'hour': final_hour }
    template = get_template('core/email.html')
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

