from django import forms
from django.core.exceptions import ValidationError
import re

class Studentform(forms.Form):
    name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    email = forms.EmailField()
    contact = forms.CharField(max_length=15)
    image = forms.ImageField()
    document = forms.FileField()

    # --- Field-level validations ---
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(" ", "").isalpha() :
            raise ValidationError("Name should only contain letters and spaces.")
        return name
    
    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city.replace(" ", "").isalpha() :
            raise ValidationError("Name should only contain letters and spaces.")
        return city

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.lower().endswith(('@gmail.com','@yahoo.com')):
            raise ValidationError("Only gmail and yahoo addresses are allowed.")
        
        return email

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not re.match(r'^\d{10}$', contact):
            raise ValidationError("Contact must be a 10-digit number.")
        return contact

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 2 * 1024 * 1024:
            raise ValidationError("Image size should not exceed 2MB.")
        elif image and not image.name.lower().endswith(('.jpeg', '.png','jpg')):
            raise ValidationError("Image must be either .jpeg or .png")
        return image

    def clean_document(self):
        document = self.cleaned_data.get('document')
        if document and not document.name.lower().endswith(('.pdf','.doc','.docx')):
            raise ValidationError("Only PDF.DOC and DOCX files are allowed.")
        return document