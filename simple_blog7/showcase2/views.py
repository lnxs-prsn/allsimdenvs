from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects':projects})


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
        #lots of code is missing as AI did not provide it.
        form.save()
        return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

    