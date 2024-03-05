"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operation.views import HelloWorldView,GoodMorningView,GoodAfternoonView,GoodEveningView,GoodNightView,AdditionView,SubtractionView,ProductView,DivisionView,CubeView,LeapYearView,ArmstrongView,PrimeNumberView,\
LongestWordView,ValidParanthesesView,HighestCharacterView,PowerView,SignUpView,LoginView,EmiCalculatorView,HomeView



urlpatterns = [
    path('',HomeView.as_view()),
    path('admin/', admin.site.urls),  #path('route','View','name')
    path('helloworld/',HelloWorldView.as_view()),
    path('goodmorning/',GoodMorningView.as_view()),
    path('goodafternoon/',GoodAfternoonView.as_view()),
    path('goodevening/',GoodEveningView.as_view()),
    path('goodnight/',GoodNightView.as_view()),
    path('addition/',AdditionView.as_view(),name='add'),
    path('subtraction/',SubtractionView.as_view(),name='sub'),
    path('product/',ProductView.as_view(),name='product'),
    path('division/',DivisionView.as_view(),name='div'),
    path('cube/',CubeView.as_view(),name='cube'),
    path('leapyear/',LeapYearView.as_view(),name='leap'),
    path('armstrong/',ArmstrongView.as_view(),name='arm'),
    path('primenumber/',PrimeNumberView.as_view(),name='prime'),
    path('longestword/',LongestWordView.as_view(),name='long'),
    path('validparantheses/',ValidParanthesesView.as_view(),name='valid'),
    path('highestcharacter/',HighestCharacterView.as_view(),name='longch'),
    path('power/',PowerView.as_view(),name='power'),
    path('signup/',SignUpView.as_view()),
    path('login/',LoginView.as_view()),
    path('emi/',EmiCalculatorView.as_view(),name='emi')
    
]
