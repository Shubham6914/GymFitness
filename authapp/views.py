from django.shortcuts import render,redirect
# for messages i have import messages framework form django contrib 
from django.contrib import messages
#importing user from django auth models which is inbulit in django 
from django.contrib.auth.models import User 
# iam using django built in authentication User model that's why here i have import these inbuilt functionality
# of authenticate function, login and logout 
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def Home(request):
   return render(request, "index.html")



def Signup(request):
   if request.method == "POST":
      username  = request.POST.get('email')
      phonenumber = request.POST.get('phonenumber')
      password1 = request.POST.get('password1')
      password2 = request.POST.get('password2')
      
      if len(phonenumber) > 10 or len(phonenumber) < 10:
         messages.info(request, "Phone Number Must be 10 Digits")
         return redirect("signup")
      if password1 != password2:
         messages.info(request, "password does not Match")
         return redirect("signup")
      try:
         if User.objects.get(username=username):
            messages.warning(request,"Email is already taken")
            return redirect("signup")
      except Exception as identifier:
         pass
      try:
         if User.objects.get(phonenumber=phonenumber):
            messages.warning(request,"Phone Number is akready taken ")
            return redirect("signup")
      except Exception as identifier:
         pass
      myuser = User.objects.create_user(username ,phonenumber,password1)
      myuser.save()
      messages.success(request,"User is Created please login")
      return redirect("login")
   return render(request, "signup.html")

def Login(request):
   if request.method =="POST":
      username = request.POST.get('email')
      password1 = request.POST.get('password1')
      myuser = authenticate(username=username,password=password1)
      if myuser is not None:
         login(request,myuser)
         messages.success(request, "Login Successfully")
         return redirect("home")
      else:
         messages.error(request, "Invalid Credentials") 
         return redirect("login") 
   return render(request, "login.html")


def Logout(request):
   logout(request)
   messages.success(request,"Logout Successfully")
   return redirect("login")