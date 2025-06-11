print("From app/views.py files....")



from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponse,JsonResponse
import json

# Create your views here.
# def home(req):
#     return HttpResponse("<h1 style='color:red'>This is home</h1>")

# def about(req):
#     return HttpResponse("<h1 style='color:red'>This is about</h1>")

# def contact(req):
#     return HttpResponse("<h1 style='color:red'>This is contact</h1>")

# def myrender(req):
#     # context={'name':"Harsh"}
#     # response=render(req,'home.html',context)
#     # return response
#     return redirect('https://github.com/harsh14thakre')
    # return render(req,'home.html',context)
    # return HttpResponse("<h1 style='color:red'>This is services</h1>")


# def home(req):
#     data=[{'name':'Harsh','age':20},{'name':'Ashish','age':23},{'name':'Dharmendra','age':22}]
#     # data1={'name':'Jai','age':25}
#     # return HttpResponse(da)
#     # j_data= json.dumps(data)
#     # return HttpResponse(j_data,content_type='application/json')
#     return JsonResponse(data,safe=False)


# def home(req):
#     # return render(req,'home.html')
#     # return redirect('home',"Harsh")
#     return redirect('home1',"Harsh")


# def home1(req,pk):
#     context={}
#     context['x']=pk
#     return render(req,home.html,context)


# def home(req):
#     return redirect('home1',10)

# def about(req,x):
#     context={}
#     context['first']=x
#     return render(req,'home.html',context)


from django.urls import reverse
from urllib.parse import urlencode
def home(req):
    base_url = reverse('redirect1')
    query_string = urlencode({'name': 'Harsh', 'age': 37})
    return redirect(f"{base_url}?{query_string}")
def redirect1(req):
    print(req.method)
    print(req.GET)
    print(req.POST)
    print(req.META)
    print(req.COOKIES)