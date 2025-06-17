from django import forms 

class Studentform(forms.Form):
    name=forms.CharField(max_length=50)
    city=forms.CharField(max_length=50)
    email=forms.EmailField()
    contact=forms.IntegerField()
    image=forms.ImageField()
    document=forms.FileField()