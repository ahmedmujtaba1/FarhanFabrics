from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'farhanfarbicsapp/home.html')

def about_us(request):
    return render(request, 'farhanfarbicsapp/about_us.html')

def projects(request):
    return render(request, 'farhanfarbicsapp/project.html')

def contact_us(request):
    return render(request, 'farhanfarbicsapp/contact_us.html')

def team(request):
    return render(request, 'farhanfarbicsapp/team.html')

def achivements(request):
    return render(request, 'farhanfarbicsapp/blog.html')