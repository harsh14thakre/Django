from django.shortcuts import render

# Create your views here.

from .forms import Studentform

def home(req):
    if req.method=='POST':
        print("Hii.............")
        print(req.POST)
        form=Studentform(req.POST, req.FILES)
        if form.is_valid():
            #  a=form.cleaned_data['Stu_name']
            #  b=form.cleaned_data['Stu_city']
            #  c=form.cleaned_data['Stu_email']
            #  d=form.cleaned_data['Stu_contact']
            #  e=form.cleaned_data['Stu_image']
            #  f=form.cleaned_data['Stu_document']
            #  print(a,b,c,d,e,f)
             a=req.POST.get['Stu_name']
             b=req.POST.get['Stu_city']
             c=req.POST.get['Stu_email']
             d=req.POST.get['Stu_contact']
             e=req.FILES.get['Stu_image']
             f=req.FILES.get['Stu_document']
             print(a,b,c,d,e,f)

    else:
        form=Studentform()
        return render(req,'home.html',{'fm':form})

# def data(req):
#     return render(req,'data.html')