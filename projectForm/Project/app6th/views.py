from django.shortcuts import render,redirect

# Create your views here.
from .models import Student
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        detail = request.POST.get('detail')
        phone = request.POST.get('phone')
        education = request.POST.getlist('subscribe')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        profile_pic = request.FILES.get('profile-pic')
        resume = request.FILES.get('resume')
        user = Student.objects.filter(email=email)
        if user:
            return render( request,'register.html') 
        else:
            if password == cpassword:
                Student.objects.create(name=name,email=email,detail=detail,phone=phone,education=education,gender=gender,dob=dob,profile_pic=profile_pic,resume=resume,password=password)
                return redirect('login')

            else:
                return redirect('register')
    else:
        return render(request,'register.html')
    

def login(request):
    return render(request,'login.html')    

def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password, )