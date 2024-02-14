from django.shortcuts import render,redirect
# for messages i have import messages framework form django contrib 
from django.contrib import messages
#importing user from django auth models which is inbulit in django 
from django.contrib.auth.models import User 
# iam using django built in authentication User model that's why here i have import these inbuilt functionality
# of authenticate function, login and logout 
from django.contrib.auth import authenticate,login,logout
from authapp.models import contact,MembershipPlan,Trainer,Enrollment,Gallery,Attendance
# Create your views here.

def Home(request):
   return render(request, "index.html")


def View_Profile(request):
   if not request.user.is_authenticated:
      messages.warning(request, "Please Login and Try Again")
      return redirect('login')
   else:
      user_email = request.user
      print(user_email)
      posts = Enrollment.objects.filter(email=user_email) #filtering current user  for enroll 
      attendance = Attendance.objects.filter(email_address=user_email) # filtering current user for attendance 
      context={
         "posts":posts,
         "attendance" : attendance,
      }
      print(posts)
   return render(request, "profile.html",context)

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
         return redirect("home")
         messages.success(request, "Login Successfully")
      else:
         messages.error(request, "Invalid Credentials") 
         return redirect("login") 
   return render(request, "login.html")


def Logout(request):
   logout(request)
   messages.success(request,"Logout Successfully")
   return redirect("login")


def Contact(request):
   if request.method =="POST":
      name = request.POST.get('full_name')
      email = request.POST.get('email')
      phone_number = request.POST.get('phonenumber')
      desc = request.POST.get('desc')
      myquery = contact(name=name,email=email,phonenumber=phone_number,description=desc)
      myquery.save()
      messages.success(request, "Thanks for Contacting us we will get you back soon")
      return redirect("contact")
      
   return render(request, "contact.html")

def Enroll(request):
   if not request.user.is_authenticated:
      messages.warning(request, "Please Login and Try Again")
      return redirect('login')
   # If the user is authenticated, proceed with enrollment logic
   else:
      
      Membership = MembershipPlan.objects.all()
      SelectTrainer = Trainer.objects.all()
      context = {
         "Mebership": Membership,
         "SelectTrainer" : SelectTrainer,
      }
      if request.method == "POST":
         # Handle POST request to enroll
         # Extract data from the POST request
         username = request.POST.get('fullName')
         email = request.POST.get('email')
         gender = request.POST.get('gender')
         mobile = request.POST.get('phonenumber')
         date_of_birth = request.POST.get('DOB')
         membership = request.POST.get('select_mebership_plan')
         trainer = request.POST.get('select_trainer')
         reference = request.POST.get('reference')
         address = request.POST.get('address')
         # Create an Enrollment instance with the extracted data
         query = Enrollment(fullName=username,email=email,gender=gender,phonenumber=mobile,DOB=date_of_birth,
                           select_mebership_plan=membership,select_trainer=trainer,reference=reference,
                           address=address)
         # Save the enrollment data
         query.save()
         # Display success message
         messages.success(request, message="You have Enrolled Successfully ")
         # Redirect back to the enroll page to reset the form
         return redirect("enroll")
      # Render the enroll page with context data
   return render(request=request, template_name="enroll.html",context=context)

def gallery(request):
   posts = Gallery.objects.all()
   context = {"posts":posts}
   return render(request, "gallery.html",context)


def User_Attendance(request):
   if not request.user.is_authenticated:
      messages.warning(request, "Please Login and Try Again")
      return redirect('login')
   # If the user is authenticated, proceed with enrollment logic
   else:
      SelectTrainer = Trainer.objects.all()
      # username = request.user
      # print(username)
      context = {
         "SelectTrainer" : SelectTrainer,
      }
      if request.method == "POST":
         username = request.POST.get('email')
         select_workout = request.POST.get('workout')
         login = request.POST.get('loginTime')
         logout = request.POST.get('logoutTime')
         trained_by = request.POST.get('select_trainer')
         query = Attendance(email_address=username,login=login,logout=logout,select_workout=select_workout,trained_by=trained_by)
         query.save()
         messages.info(request, "Attendance applied successfully..!")
         return redirect("attendance")
   return render(request , "attendance.html",context)




def About(request):
   return render(request, "about.html")