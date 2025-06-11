from django.shortcuts import render
# Create your views here.

def home(request):
    return render (request,'home.html')

def data12(request):
    print(request.method)
    print(request.POST)
    print(request.GET)
    print(request.META)
    if request.method =="POST":
        n = request.POST.get('x')
        e = request.POST.get('y')
        c = request.POST.get('z')
        i = request.FILES.get('f')
        d = request.FILES.get('d')
        print(n,e,c,i,d)


    # print(request.POST)
    # print(request.FILES)
    # print(request.method)

    data={
        'name':{'key1':n},
        'email':e,
        'contact':c,
        'image':i,
        'document':d
    }
    return render(request,'data.html',{'key':data})