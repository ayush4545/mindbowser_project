from django.http import HttpResponse
from django.shortcuts import render,redirect
from login_register.models import employee,manager
from django.contrib.auth.models import User
from .forms import managerSignup,managerLogin,employeeUpdate
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.


#this function is used to displaying all the employee in the home screen
def home(request):
    data=employee.objects.all()
    
    return render(request,'home.html',{'data':data})


# this function is for signup for manager and save properites of manager
def signup(request):
    if request.method=='POST':
        fm= managerSignup(request.POST)
        if fm.is_valid():
            try:
                email=fm.cleaned_data['email']
                fname=fm.cleaned_data['fname']
                lname=fm.cleaned_data['lname']
                password=fm.cleaned_data['password']
                address=fm.cleaned_data['address']
                dob=fm.cleaned_data['dob']
                company=fm.cleaned_data['comapny']

                myuser=manager(email=email,fname=fname,lname=lname,password=password,address=address,dob=dob,company=company)
                myuser.save()
                fm= managerSignup()
            except:
                pass    
    else:
        fm= managerSignup()

    return render(request,'signup.html',{forms:fm})         
   
# this function is used for manager login 
def login(request):
    if request.method=='POST':
        fm=managerLogin(request.POST)
        if fm.is_valid():
            try:
                email=fm.cleaned_data['email']
                password=fm.cleaned_data['password']
                user=authenticate(email=email,password=password)
                obj=manager.objects.filter(email=email,password=password)

                if user is not None:
                    login(request,user)
                    messages.success(request,"Successfully login")
                    return redirect('home')
                else:
                     messages.error(request,"Invalid Credientials")   
                     return redirect('/') 
            except:
                messages.error(request,"email Id & Password are not invalid")
                return redirect('/')

    else:
            fm=managerLogin()   

    return render(request,'login.html',{'form':fm})      

# this function is used for delete the particluar employee data

#in template used dynamic url so it give id from that to this delete_Data function
def delete_data(request,id):
    if request.method=='POST':
        pi=employee.objects.get(id_no=id)
        p1.delete()
        return redirect('home')

def update_data(request,id):
    if request.method=='POST':
        pi=employee.objects.get(id_no=id)
        fm=employeeUpdate(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=employee.objects.get(id_no=id)
        fm=employeeUpdate(instance=pi)

    return render(request,'update.html',{'form':fm})        