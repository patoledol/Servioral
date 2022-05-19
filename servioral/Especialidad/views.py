from django.shortcuts import render

# Create your views here.

def especialidad(request):
    return render(request, "Especialidad/Doctors.html")