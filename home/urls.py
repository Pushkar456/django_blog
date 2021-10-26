from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('SinUp',views.SinUp,name="SinUp"),
    path('login',views.Login,name="login"),
    path('logout',views.logOut,name="logout"),
    path('about',views.about,name="about"),
    path('search',views.search,name="search")
]