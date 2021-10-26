from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('blogComment',views.BlogComment,name="blogcomment"),
    path('blogReply',views.BlogReply,name="blogrelpy"), 
    path('<str:slug>',views.post,name="post")
]