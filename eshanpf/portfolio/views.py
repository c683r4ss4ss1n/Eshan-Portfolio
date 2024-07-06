from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def services(request):
    return render(request, 'portfolio/services.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def education(request):
    return render(request, 'portfolio/education.html')

def experience(request):
    return render(request, 'portfolio/experience.html')

def work(request):
    return render(request, 'portfolio/work.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

