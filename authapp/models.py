from django.db import models

# Create your models here.

class contact(models.Model):
   name = models.CharField(max_length=25)
   email = models.EmailField()
   phonenumber = models.CharField(max_length=25)
   description = models.TextField()
   
   
   def __str__(self):
      return self.name


class Enrollment(models.Model):
   fullName = models.CharField(max_length=25)
   email = models.EmailField()
   gender = models.CharField(max_length=20)
   phonenumber = models.CharField(max_length=25)
   DOB = models.CharField(max_length=20)
   select_mebership_plan = models.CharField(max_length=300)
   select_trainer = models.CharField(max_length=55)
   reference = models.CharField(max_length=50)
   address = models.TextField()
   paymentStatus = models.CharField(max_length = 50, blank=True, null=True)
   price = models.IntegerField(blank=True,null=True)
   due_date = models.DateTimeField(blank=True,null=True)
   time_stamp = models.DateTimeField(auto_now_add=True,blank=True)
   
   
   def __str__(self):
      return self.fullName
   

class Trainer(models.Model):
   name = models.CharField(max_length=50)
   phone = models.CharField(max_length=50)
   gender = models.CharField(max_length=50)
   salary  = models.IntegerField(null=False)
   time_stamp = models.DateTimeField(auto_now_add=True,blank=True)
   
   def __str__(self):
      return self.name
   

class MembershipPlan(models.Model):
   plan = models.CharField(max_length=55)
   price = models.IntegerField()
   
   def __int__(self):
      return self.id
   
   
class Gallery(models.Model):
   title = models.CharField(max_length=30)
   image = models.ImageField(upload_to="gallery")
   time_stamp = models.DateTimeField(auto_now_add=True,blank=True)
   
   def __int__(self):
      return self.id
   
   
class Attendance(models.Model):
   email_address = models.EmailField()
   select_date = models.DateTimeField(auto_now_add=True)
   login = models.CharField(max_length=40)
   logout = models.CharField(max_length = 40)
   trained_by = models.CharField(max_length=40)
   select_workout = models.CharField(max_length=40)
   
   def __int__(self):
      return self.id
   
   