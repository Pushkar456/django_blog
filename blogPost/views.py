from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Comments
from blogPost.templatetags import extras



# Create your views here.

def index(request):
     post=Post.objects.all()
     dict1={'posts':post}
     return render(request,"blogPost.html",dict1)

def post(request,slug):
     post=Post.objects.filter(slug=slug).first()
     post.views=post.views+1
     post.save()
     comments=Comments.objects.filter(post=post,parent=None)
     replies=Comments.objects.filter(post=post).exclude(parent=None)
     replydict={}
     for reply in replies:
         if reply.parent.sno not in replydict.keys():
             replydict[reply.parent.sno]=[reply]
         else:
             replydict[reply.parent.sno].append(reply)  
            
             
     dict2={'post':post,'comments':comments,'user':request.user,'replies':replydict}
     return render(request,"post.html",dict2)
     
def BlogComment(request):
   if request.method=='POST':
     postsno=request.POST.get('postsno')
     comment=request.POST.get('comment')
     user=request.user
     post=Post.objects.get(sno=postsno)
     if len(comment)!=0:
         com=Comments(user=user,content=comment,post=post)
         com.save()
     return redirect(f"/blog/{post.slug}")

def BlogReply(request):
   if request.method=='POST':
     postsno=request.POST.get('postsno')
     reply=request.POST.get('reply')
     user=request.user
     post=Post.objects.get(sno=postsno)
     commentsno=request.POST.get("parent")
     comment=Comments.objects.get(sno=commentsno)
     if len(reply)!=0:
         com=Comments(user=user,content=reply,post=post,parent=comment)
         com.save()
     return redirect(f"/blog/{post.slug}")








