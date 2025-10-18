from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from .models import Project
from django.core.mail import send_mail
from django.conf import settings

def home_view(request):
    return render(request, 'core/home.html')

def portfolio_view(request):
    return render(request, 'core/portfolio.html')

def portfolio_view(request):
    projects = Project.objects.all()
    return render(request, 'core/portfolio.html', {'projects': projects})

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"New Contact Form Submission from {name}"
            full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

            try:
                send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                print("Email sending failed:", e)
                return HttpResponse(f"Email error: {e}")
            return render(request, 'core/contact_success.html')
    return render(request, 'core/contact.html', {'form': form})

