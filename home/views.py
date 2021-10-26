from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from blogPost.models import Post
# Create your views here.
def index(request):
      posts=Post.objects.order_by('-views')
      dict2={'posts':posts,'range':range(0,3)}
      return render(request,'home.html',dict2)

def search(request):
    query=request.GET['searchs']
    postcontent=Post.objects.filter(content__icontains=query)
    posttittle=Post.objects.filter(tittle__icontains=query)
    postauthor=Post.objects.filter(author__icontains=query)
    searchs=postcontent.union(posttittle,postauthor)
    searches={"searchs":searchs,'query':query}  
    return render(request,'search.html',searches)


def SinUp(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        mob=request.POST['mob']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 != pass2:
            messages.error(request,'passwords do not match')
            return redirect('/')
        if len(username) > 10:
            messages.error(request,'username mist be uder 10 char')
            return redirect('/')
        if len(mob) < 10 or len(mob) > 10:
            messages.error(request,'mobile no must be of 10 numbers')
            return redirect('/') 
        
        myuser=User.objects.create_user(username=username,email=email,password=pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.mobile=mob
        myuser.save()  
        messages.success(request, f'Welcome to ItsCoding world {username}')
        return redirect('/')
    else:
        return HttpResponse("404 - Not Found ")

def about(request):
      return render(request,'home.html')

def Login(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpass) 
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome to ItsCoding world {loginusername}')
            return render(request,'home.html')
        else:
            messages.error(request, 'Invalid info,plaese try again')
            return render(request,'home.html')
    else:
        return HttpResponse("404 - Not Found ")

def logOut(request):
      logout(request)
      return render(request,'home.html')


        

