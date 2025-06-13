from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('registerup/', views.registerup, name='registerup'),
    path('loginup/',views.loginup,name ='loginup'),
    path('home/',views.home,name ='home'),
    path('booking/',views.booking,name = "booking"),
    path('bookingup/',views.bookingup,name="bookingup"),
    path('sucessfully/',views.sucessfully,name ='sucessfully'),
    path('signout/',views.signout,name='signout'),
    path('about/',views.about,name='about'),
]
