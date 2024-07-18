from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    return render(request, 'showcase/home.html', {'projects':projects})

def about(request):
    return render(request, 'showcase/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('thanks')
    else:
        form = ContactForm()
    return render(request, 'showcase/contact.html', {'form':form})


def thanks(request):
    return render(request, 'showcase/thanks.html')