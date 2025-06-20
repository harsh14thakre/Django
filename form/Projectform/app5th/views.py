from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

from .forms import Studentform
from .models import Student

def home(req):
    if req.method=='POST':
        print("Django.........")
        print(req.POST)
        form=Studentform(req.POST, req.FILES)
        if form.is_valid():
             print(form.cleaned_data)
            #  a=req.POST.get['Stu_name']
            #  b=req.POST.get['Stu_city']
            #  c=req.POST.get['Stu_email']
            #  d=req.POST.get['Stu_contact']
            #  e=req.FILES.get['Stu_image']
            #  f=req.FILES.get['Stu_document']
             name=form.cleaned_data['name']
             city=form.cleaned_data['city']
             email=form.cleaned_data['email']
             contact=form.cleaned_data['contact']
             image=form.cleaned_data['image']
             document=form.cleaned_data['document']
             user=Student.objects.filter(email=email)
            #  print(n,c,e,o,i,d)
             if user:
                msg="Email already exit"
                form=Studentform()
                return render(req ,'home.html',{'msg':msg,'fm':form })
             else:
                Student.objects.create(name=name,city=city,email=email,contact=contact,image=image,document=document)
                msg=" Data Successfully saved in DataBase "
                form=Studentform()
                return render(req,'home.html',{'msg':msg,'fm':form})
                # return HttpResponse(f"<h1> Data Successfully saved in DataBase </h1>")
             
        else:
             return render(req,'home.html',{'fm':form})

    else:
        form=Studentform()
        return render(req,'home.html',{'fm':form})

# def data(req):
#     return render(req,'data.html')