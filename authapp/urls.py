from django.urls import path,include
from authapp import views
urlpatterns = [
  path('',views.Home, name="home"),
  path('signup/', views.Signup, name='signup'),
  path('login/', views.Login, name='login'),
  path('logout/', views.Logout, name='logout'),
  path('contact/', views.Contact, name='contact'),
  path('enroll/', views.Enroll, name='enroll'),
  path('profile/', view=views.View_Profile, name='profile'),
  path('gallery/', view=views.gallery, name='gallery'),
  path('attendance/', view=views.User_Attendance, name='attendance'),
  path('about/', view=views.About, name='about'),
]
