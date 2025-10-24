from django import forms
import re

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre completo",
        max_length=100,
        help_text="Solo letras y espacios. Ejemplo: Juan Pérez"
    )
    email = forms.EmailField(
        label="Correo electrónico",
        help_text="Debe ser un correo válido (ejemplo: usuario@dominio.com)"
    )
    telefono = forms.CharField(
        label="Teléfono",
        max_length=15,
        help_text="Formato: +34 600123456 o 600123456",
        widget=forms.TextInput(attrs={'placeholder': 'Ej: +34 600123456'})
    )

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', nombre):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not re.match(r'^(?:\+?\d{1,3})?\s?\d{9}$', telefono):
            raise forms.ValidationError("Formato de teléfono no válido. Ejemplo: +34 600123456")
        return telefono