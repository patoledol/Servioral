import email
from email import message
from pickle import TRUE
from django import forms
from .models import cita
from Odontologo.models import odontologo
from Especialidad.models import especialidad

class CitaForm(forms.ModelForm):

    paciente = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Nombre'}
    ))
    phone = forms.CharField(label="Teléfono", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control','placeholder':'Teléfono'}
    ))
    id_doc = forms.ModelChoiceField(queryset=odontologo.objects.all(), empty_label="Doctor(a)", widget=forms.Select(
        attrs={'class':'form-control','placeholder':'Doctor'}
    ))
    espe = forms.ModelChoiceField(queryset=especialidad.objects.all(), empty_label="Servicio", widget=forms.Select(
        attrs={'class':'form-control','placeholder':'Especialidad'}
    ))
    date = forms.DateField(label="Fecha", required=True, widget=forms.DateInput(
        attrs={'class':'form-control','placeholder':'Fecha', 'type':'date'}
    ))
    hour = forms.TimeField(label="Hora", required=True, widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'Hora', 'type':'time'}
    ))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Email'}
    ))
    status = forms.HiddenInput( attrs={'class':'form-control','placeholder':'Estado'})
    
    class Meta:
        model = cita
        fields = '__all__'
 
  
  
  
    
    # email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
    #     attrs={'class':'form-control','placeholder':'Email'}
    # ))
    # date = forms.DateTimeField(label="Asunto", required=True, widget=forms.TextInput(
    #     attrs={'class':'form-control','placeholder':'Asunto'}
    # ))
    # message = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
    #     attrs={'class':'form-control','placeholder':'Mensaje', 'row': 5}
    # ))
    # status = forms.HiddenInput( attrs={'class':'form-control','placeholder':'Estado'})

    # class Meta:
    #     model = cita
    #     fields = '__all__'


