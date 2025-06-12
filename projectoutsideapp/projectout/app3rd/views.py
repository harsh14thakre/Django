# from django.shortcuts import render
# # Create your views here.

# def home(request):
#     if request.method =="POST":
#          e = request.POST.get('y')
#          c = request.POST.get('z')
#          n = request.POST.get('x')
#          i = request.FILES.get('f')
#          d = request.FILES.get('d')
#          print(n,e,c,i,d)
#          data={
#              'name':{'key1':n},
#              'email':e,
#              'contact':c,
#              'image':i,
#              'document':d
#          }
#          return render(request,'home.html',{'key':data})
#     return render(request,'home.html')

# def data12(request):
#     print(request.method)
#     print(request.POST)
#     print(request.GET)
#     print(request.META)
    # if request.method =="POST":
    #     n = request.POST.get('x')
    #     e = request.POST.get('y')
    #     c = request.POST.get('z')
    #     i = request.FILES.get('f')
    #     d = request.FILES.get('d')
    #     print(n,e,c,i,d)


    # # print(request.POST)
    # # print(request.FILES)
    # # print(request.method)

    # data={
    #     'name':{'key1':n},
    #     'email':e,
    #     'contact':c,
    #     'image':i,
    #     'document':d
    # }
    # return render(request,'data.html',{'key':data})

from django.shortcuts import render

# Create your views here.
def home(request):
      if request.method == "POST":
            n =request.POST.get('x')
            e =request.POST.get('y')
            c =request.POST.get('z')
            i =request.FILES.get('f')
            d =request.FILES.get('d')
            data={
                  'name':{'key1':n},
                  'email':{'key2':e},
                  'contact':c,
                  'image':i,
                  'document':d
            }
            data1 = {'name':'Neeraj','email':'neeraj@gmail.com','contact':9424444348,'image':True,'document':False}
            print(n,e,c,i,d) 
            data2 = {
                  'key1':data,
                  'key2':data1
            }
            # return render(req,'home.html',{'key1':data})
            return render(request,'home.html',{'key2':data,'key1':data1})

      return render(request,'home.html')

# def data(request):
#       if request.method == "POST":
#             n =request.POST.get('x')
#             e =request.POST.get('y')
#             c =request.POST.get('z')
#             i =request.FILES.get('f')
#             d =request.FILES.get('d')
#             data={
#                   'name':{'key1':n},
#                   'email':{'key2':e},
#                   'contact':c,
#                   'image':i,
#                   'document':d

#             }
#             print(n,e,c,i,d) 
#             return render(request,'home.html',{'key':data})
#             return render(request,'home.html',{'key1':data})
#             return render(request,'home.html',{'key2':data1})