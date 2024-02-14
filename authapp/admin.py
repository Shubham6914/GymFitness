from django.contrib import admin
from authapp.models import contact,MembershipPlan,Enrollment,Trainer,Gallery,Attendance
# Register your models here.

@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
   list_display = ['id','name','email','phonenumber','description']


@admin.register(Enrollment)

class AdminEnrollment(admin.ModelAdmin):
   list_display = ['id','fullName','email','gender','phonenumber','DOB',
                   'select_mebership_plan','select_trainer','reference','address','paymentStatus',
               'price','due_date','time_stamp']
   

@admin.register(MembershipPlan)

class AdminMembership(admin.ModelAdmin):
   list_display = ['id','plan','price']
   
   
@admin.register(Trainer)
   
class AdminTrainer(admin.ModelAdmin):
   list_display = ['id','name','phone','gender','salary','time_stamp']
   
   
   
@admin.register(Gallery)
class AdminGallery(admin.ModelAdmin):
   list_display = ['id','title','image','time_stamp']
   
   
   
@admin.register(Attendance)

class AdminAttendance(admin.ModelAdmin):
   list_display = ['id','email_address','select_date','login','logout','trained_by','select_workout']