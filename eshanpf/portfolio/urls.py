from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('skills/', views.skills, name='skills'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('work/', views.work, name='work'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
