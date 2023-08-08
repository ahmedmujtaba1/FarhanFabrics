from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about_us/',views.about_us,name="about_us"),
    path('projects/',views.projects,name="projects"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('team/',views.team,name="team"),
    path('achivements/',views.achivements,name="achivements"),
]

