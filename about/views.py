from django.shortcuts import render
from .models import Profile

# Create your views here.
def about(request):
    profile = Profile.objects.first()

    if not profile:
        profile = {
            'name': 'Ernesto',
            'bio': 'Web Content Migration Specialist with a passion for Django, Bootstrap, and IT leadership.',
            'profile_pic': None,
            'resume': None,
        }

    skills = [
        'Django & Bootstrap',
        'Project Management',
        'Workflow Automation',
        'Security Best Practices',
        'Content Migration',
        'Copilot Collaboration',
    ]

    return render(request, 'about.html', {'profile': profile, 'skills': skills})

