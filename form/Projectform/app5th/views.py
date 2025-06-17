from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .forms import Studentform
from .models import Student
def home(req):
    if req.method=='POST':
        print("Hii.............")
        print(req.POST)
        form=Studentform(req.POST, req.FILES)
        if form.is_valid():
             print(form.cleaned_data)
             name=form.cleaned_data['name']
             city=form.cleaned_data['city']
             email=form.cleaned_data['email']
             contact=form.cleaned_data['contact']
             image=form.cleaned_data['image']
             document=form.cleaned_data['document']
             Student.objects.create(name=name,city=city,email=email,contact=contact,image=image,document=document)
            #  return render(req,'home.html',{'fm':form})
             return HttpResponse(f"Data succesfully saved in database")
             
            #  print(a,b,c,d,e,f)
            #  a=req.POST.get['Stu_name']
            #  b=req.POST.get['Stu_city']
            #  c=req.POST.get['Stu_email']
            #  d=req.POST.get['Stu_contact']
            #  e=req.FILES.get['Stu_image']
            #  f=req.FILES.get['Stu_document']
            #  print(a,b,c,d,e,f)

    else:
        form=Studentform()
        return render(req,'home.html',{'fm':form})

# def data(req):
#     return render(req,'data.html')