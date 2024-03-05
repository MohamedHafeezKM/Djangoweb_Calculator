from django.shortcuts import render #deafult imported
from math import ceil,pow    #ceil-rounding, pow-power,rays to (x**2)
from django.views.generic import View   #imported
from django import forms     #imported django.forms.py
# Create your views here.
class OperationForm(forms.Form):    #(filename.class) format 
    num1=forms.IntegerField() #django create text box and label,we don't have to create it
    num2=forms.IntegerField()  #usage of forms.Form

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')

class PowerView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()    #new object-form
        return render(request,'power.html',{'output':form})
    def post(self,request,*args,**kwargs):
        form=OperationForm(request.POST)
        if form.is_valid():
            result=form.cleaned_data.get('num1')**form.cleaned_data.get('num2')
        else:
            result='not valid nos'
        return render(request,'power.html',{'output':form,'result':result})
    
class EmiForm(forms.Form):
    loan_amount=forms.IntegerField()
    tenure=forms.IntegerField()
    intrest_rate=forms.IntegerField()
    
class EmiCalculatorView(View):
    def get(self,request,*args,**kwargs):
        form=EmiForm()
        return render(request,'emicalculator.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=EmiForm(request.POST)
        if form.is_valid():
            sectionA=form.cleaned_data.get('loan_amount')*((form.cleaned_data.get('intrest_rate')/12)/100)
            sectionB=pow(1+((form.cleaned_data.get('intrest_rate')/12)/100),form.cleaned_data.get('tenure')*12)
            sectionC=pow(1+((form.cleaned_data.get('intrest_rate')/12)/100),form.cleaned_data.get('tenure')*12)
            # print(sectionA)
            # print(sectionB)
            # print(sectionC)
            result=round((sectionA*sectionB)/(sectionC-1))
           

        else:
            result='invalid'

        return render(request,'emicalculator.html',{'form':form,'result':result})


    

class RegistrationForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()
    confirm_password=forms.CharField()

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,'register.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
        else:
            print('Form is incorrect')

        return render(request,'register.html',{'form':form})
    
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)   #initilising (take only needed, token not needed)

        if form.is_valid():  #is_valid ,default fn in django.forms.py
            print(form.cleaned_data)
            #.cleaned_data is a part of .is_valid()
        else:
            print('Form has error')
        
        return render(request,'login.html',{'form':form})  #return back to our page


class HelloWorldView(View):

    def get(self,request,*args,**kwargs):
        return render(request,'helloworld.html')
    

class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'goodmorning.html')
    

class GoodAfternoonView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'goodafternoon.html')
    
class GoodEveningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'goodevening.html')
    
class GoodNightView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'goodnight.html')
    


class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'addition.html')
    
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("Number1"))
        n2=int(request.POST.get("Number2"))
        result=n1+n2
        return render(request,'addition.html',{'output':result})
    

class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'sub.html')
    
    def post(self,request,*args,**kwargs): #request.POST is a dictionery, default python file from WSGI Request file
        #request.POST={csrf:token,'Number1':100,'Number2;:300}
        # print(request.POST)  # to check
        n1=int(request.POST.get("Number1"))
        n2=int(request.POST.get("Number2"))
        # print(n1)
        # print(n2)
        if n1>n2:
            result=n1-n2
        else:
            result=n2-n1
        
        return render(request,'sub.html',{'output':result})
    

class ProductView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'product.html')
    
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get('Number1'))
        n2=int(request.POST.get('Number2'))
        result=n1*n2
        print(result)
        return render(request,'product.html',{'output':result})
    
class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'div.html')
    
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get('Number1'))
        n2=int(request.POST.get('Number2'))
        if n1>n2:
            result=n1/n2

        else:
            result=n2/n1
        
        return render(request,'div.html',{'output':result})

    
class CubeView(View):

    def get(self,request,*args,**kwargs):
        return render(request,'cube.html')
    
    def post(self,request,*args,**kwargs):
        print(request.POST)
        n1=int(request.POST.get('Number1'))
        result=n1**3
        return render(request,'cube.html',{'output':result})



class LeapYearView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'leapyear.html')
    
    def post(self,request,*args,**kwargs):
        year=int(request.POST.get('Year'))

        if((year%400==0) or (year%100!=0) and (year%4==0)):
            result='Leap year'
        else:
            result='Not a leap year'

        return render(request,'leapyear.html',{'output':result})


class ArmstrongView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'armstrong.html')
    
    def post(self,request,*args,**kwargs):
        num=int(request.POST.get('Number1'))
        original=num
        sum=0

        while(num!=0):
            last_digits=num%10
            cube=last_digits**3
            sum=sum+cube
            num=num//10
        

        if sum==original:
            result='The number you enetered is an Armstrong number'
        

        else:
            result='The number you enetered is not an Armstrong number'
        
        return render(request,'armstrong.html',{'output':result})

class PrimeNumberView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'primeno.html')

    def post(self,request,*args,**kwargs):
        num=int(request.POST.get('Number')) 
        if num in [0,1]:
            result='The number is not prime number'
        elif num==2:
            result='The number is a prime number'
        else:
            for i in range(2,num):
                if num%i==0:
                    result='The number is not prime number'
                    break
                else:
                    result='The number is a prime number'

        print(result)
                
        return render(request,'primeno.html',{'output':result})    
        
class LongestWordView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'longestword.html') 
    
    def post(self,request,*args,**kwargs):
        words=request.POST.get("words").split(" ")
        result=max(words,key=lambda w:len(w))
        return render(request,'longestword.html',{'output':result})
            

class ValidParanthesesView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'validparantheses.html')

    def post(self,request,*args,**kwargs):
        value=request.POST.get('words') 
        l=len(value)
        i=0
        while (i<l):
            if l%2!=0:
                 result='not valid'
                 break


            elif value[i]=='[' and value[i+1]==']':
                result='valid'
                i+=2 
            
        

            elif value[i]=='(' and value[i+1]==')': 
                result='valid'
                i+=2

            elif value[i]=='{' and value[i+1]=='}': 
                result='valid'
                i+=2

            elif value[i]=='<' and value[i+1]=='>': 
                result='valid'
                i+=2

            else:
                result='not valid'
                break

        return render(request,'validparantheses.html',{'output':result})
            

class HighestCharacterView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'highestcharacter.html')
    
    def post(self,request,*args,**kwargs):
        character=request.POST.get("words")
        # print(character)
        wc={}

        for ch in character:
            if ch in wc:
                wc[ch]+=1
            else:
                wc[ch]=1
        # print(wc)
        if ' ' in wc:
            wc.pop(' ')
        
        
        
        for k in wc:
                if wc.get(k)==1:
                    result='None'
                else:
                    result=max(wc,key=lambda w:wc.get(w))
                    break 
            
        return render(request,'highestcharacter.html',{'output':result})
            
    
    






