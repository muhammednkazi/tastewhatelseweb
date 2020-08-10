# 78 completed


# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contactus
from videos.models import video
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# template fucntions below.
def homepage(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name'] #or request.POST.get('name','')
        email=request.POST['email'] 
        phone=request.POST['phone'] 
        desc=request.POST['desc'] 
        # print(name, email, phone, desc)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, 'Please fill all the details correctly!')
        else:
            data_contact=contactus(name=name,email=email,phone=phone,desc=desc) #to create a query
            data_contact.save() #to store in database
            messages.success(request, f'Your Reference id is {data_contact.msg_id}. We\'ll get back to you soon!')
    return render(request,'home/contact.html')    

def search(request):
    query=request.GET['query']
    print(query)
    try:
        if len(query)>78:
            data=[]
            print("query lenght more than 78 chars")
        #if searched query is present in video title or video content
        elif video.objects.filter(title__icontains=query) or video.objects.filter(content__icontains=query):
            dataTitle=video.objects.filter(title__icontains=query) 
            dataContent= video.objects.filter(content__icontains=query)
            data=dataTitle.union(dataContent) #joining both to one variable
            print("Found in Database")
        else: #if searched query is NOT present in video title or video content
            data=[]
            print("not found in db")
    except Exception as e:
        print(e)
    param={'data':data,"query":query}
    return render(request, 'home/search.html',param)

# user authentication functions below
def handleSignup(request):
    if request.method=='POST':
        fname=request.POST['fname'] #or request.POST.get('name','')
        lname=request.POST['lname']
        email=request.POST['email'] 
        phone=request.POST['phone'] 
        password=request.POST['password'] 
        cpassword=request.POST['cpassword'] 
        # print(name, email, phone, desc)
        if len(fname)<3 or len(email)<3 or len(phone)<10 or len(email)<4:
            messages.error(request, 'Please fill all the details correctly!')
        else: #create the user
            myuser=User.objects.create_user(email, email, password) #to create a user
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save() #to store in database
            messages.success(request, f'your account is created successfully')
    else:
        return HttpResponse("404 - Not Found")
    return render(request,'home/index.html')
    
def handleLogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email, password)
        user=authenticate(username=email,password=password) #validating user
        print(user)
        if user is not None: #returns None if not found.
            login(request,user)
            messages.success(request,f"Welcome {user.first_name +'  ' + user.last_name}")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials. Please Try Again!")
            return redirect('/')
    else:
        return HttpResponse("404 - Not Found")
    
def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')
