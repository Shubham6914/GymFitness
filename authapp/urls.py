from django.urls import path,include
from authapp import views
urlpatterns = [
  path('',views.home, name="home"),
]
