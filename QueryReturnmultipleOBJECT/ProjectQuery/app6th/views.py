from django.shortcuts import render
from .models import Student as stu

# Create your views here. 
def home(req):
    # all_data=stu.objects.order_by('-name')
    # print(all_data)
    all_data=stu.objects.exclude(name="Harsh")
    print(type(all_data))
    for i in all_data:
        print(i.name)
        print(i.email)
        print(i.contact)
        print(i.city)
        # print(all_data.values_list())

        return render(req,'home.html',{'data':all_data})
        




