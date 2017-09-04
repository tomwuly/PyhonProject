from django.shortcuts import render
from django.http import HttpResponse
from cmdb import models
# Create your views here.

# user_list=[
#     {"user":"jack","pwd":"abc"},
#     {"user":"tom","pwd":"ABC"},
# ]
def index(request):
    #return render(request,"index.html")
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        #print(username,password)
        # temp = {"user":username,"pwd":password}
        # user_list.append(temp)
        models.user_info.objects.create(user=username,pwd=password)
    user_list = models.user_info.objects.all()
    return render(request,"index.html",{"data":user_list})