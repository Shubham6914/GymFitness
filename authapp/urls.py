from django.urls import path,include
from authapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('',views.Home, name="home"),
  path('signup/', views.Signup, name='signup'),
  path('login/', views.Login, name='login'),
  path('logout/', views.Logout, name='logout'),
  path('contact/', views.Contact, name='contact'),
  path('enroll/', views.Enroll, name='enroll'),
  path('profile/', view=views.View_Profile, name='profile'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
