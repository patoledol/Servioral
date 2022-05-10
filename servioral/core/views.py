from django.shortcuts import render, HttpResponse
#from .models import visitas
from datetime import datetime
# Create your views here.

def home(request):
    site_web = "Home"
    return render(request, "core/index.html")

# def aboutus(request):

#     site_web = "Sobre"
#     num_visits_about = request.session.get('num_visits_about', 0)
#     request.session['num_visits_about'] = num_visits_about + 1
#     date = datetime.today().strftime('%Y-%m-%d')
#     views_about = visitas(sitio_web = site_web, contador = num_visits_about, fecha = date)
#     views_about.save()

#     return render(request, "core/about.html")

